from flask import Flask
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme='Bearer')
tokens = {
    "58fddba0-ed80-42da-b276-7b3144c2374d": "john",
    "ea1832e0-2548-400d-97a1-b8cc88fb0475": "susan"
}


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


def create_app():
    app = Flask(__name__)

    @app.get('/')
    @auth.login_required
    def index():
        return f"Hello, {auth.current_user()}!"

    return app
