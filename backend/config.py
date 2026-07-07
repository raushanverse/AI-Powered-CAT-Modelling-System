import os
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

class Config:

    # Flask Configuration
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Database Configuration
    DB_CONFIG = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME")
    }

    # JWT Configuration (Future Use)
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "cat-modelling-jwt-secret")

    # Swagger
    SWAGGER = {
        "title": "CAT Modelling System API",
        "uiversion": 3
    }