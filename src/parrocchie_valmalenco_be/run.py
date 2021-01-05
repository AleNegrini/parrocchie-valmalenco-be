import os
from flask import Flask
from flask_cors import CORS

# import app endpoints
from src.parrocchie_valmalenco_be.endpoints.mic_config.config_handler import configMic_blueprint


# create the Flask application and enable CORS
app = Flask(__name__)
CORS(app)

# Blueprints registration
app.register_blueprint(configMic_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
