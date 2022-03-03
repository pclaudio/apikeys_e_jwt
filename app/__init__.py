from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from http import HTTPStatus


def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "Kenzi3"
    jwt = JWTManager(app)

    @app.post("/auth")
    def login():
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        if username != "test" or password != "test":
            return jsonify({"msg": "Bad username or password"}), HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=username)

        return jsonify(access_token=access_token)

    @app.get("/protected")
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()

        return jsonify(logged_in_as=current_user), HTTPStatus.OK

    return app
