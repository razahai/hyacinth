from flask import Flask

from .blueprints import printing_bp, auth_bp
from .db import db

def create_app(*, testing=False) -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev"
    if testing:
        app.config["TESTING"] = True
        app.config.from_pyfile("test-config.py")
    else:
        app.config.from_pyfile("config.py")

    db.init_app(app)

    app.register_blueprint(printing_bp)
    app.register_blueprint(auth_bp)

    return app