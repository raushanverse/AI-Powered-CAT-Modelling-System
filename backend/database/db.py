import mysql.connector
from config import Config


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_CONFIG["host"],
            user=Config.DB_CONFIG["user"],
            password=Config.DB_CONFIG["password"],
            database=Config.DB_CONFIG["database"]
        )

        if connection.is_connected():
            print("✅ Database Connected Successfully")

        return connection

    except mysql.connector.Error as err:
        print(f"❌ Database Connection Error: {err}")
        return None