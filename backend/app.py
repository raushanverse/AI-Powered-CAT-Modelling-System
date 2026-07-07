from flask import Flask
from routes.user_routes import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)

@app.route("/")
def home():
    return {
        "message": "CAT Modelling System API Running Successfully 🚀"
    }

if __name__ == "__main__":
    app.run(debug=True)