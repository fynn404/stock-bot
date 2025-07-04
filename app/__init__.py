from flask import Flask
from app.routes import main_blueprint
from config import SECRET_KEY,STATIC_DIR

def create_app():
    app = Flask(__name__,static_folder=STATIC_DIR)
    app.secret_key = SECRET_KEY
    app.register_blueprint(main_blueprint)
    return app
