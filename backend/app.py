from flask import Flask

from config import Config
from extensions import cors, jwt, swagger
from routes.user_routes import user_bp
from logger import logger
from routes.auth_routes import auth_bp


def create_app():

    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(Config)

    # Initialize Extensions
    cors.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)

    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        return {
            "status": "success",
            "message": "CAT Modelling System API Running Successfully 🚀"
        }

    print(app.url_map)

    return app

app = create_app()

app.logger.handlers = logger.handlers
app.logger.setLevel(logger.level)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=False
    )