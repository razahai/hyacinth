from flask import Flask, render_template

from .blueprints import printing_bp

def create_app(*, testing=False) -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev"
    if testing:
        app.config["TESTING"] = True
        app.config.from_pyfile("test-config.py")
    else:
        app.config.from_pyfile("config.py")

    app.register_blueprint(printing_bp)

    return app