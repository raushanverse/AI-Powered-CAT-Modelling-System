from flask import Flask

from config import Config
from extensions import cors, jwt, swagger
from routes.user_routes import user_bp
from logger import logger


def create_app():
    """
    Application Factory
    """

    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(Config)

    # Initialize Extensions
    cors.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)

    # Register Blueprints
    app.register_blueprint(user_bp)

    # Home Route
    @app.route("/")
    def home():
        logger.info("Home API Accessed")

        return {
            "status": "success",
            "message": "CAT Modelling System API Running Successfully 🚀"
        }

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=False)