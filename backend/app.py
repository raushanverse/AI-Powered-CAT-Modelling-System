from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "AI Powered CAT Modelling System Backend is Running Successfully!"

    return app