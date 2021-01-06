import os
from flask import Flask
from flask_cors import CORS


def create_app():
    # create the Flask application and enable CORS
    app = Flask(__name__)
    CORS(app)

    register_blueprints(app)
    return app


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from src.parrocchie_valmalenco_be.api.config_mic import configMic_blueprint

    app.register_blueprint(configMic_blueprint)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
