from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

from src.parrocchie_valmalenco_be.utils.config_handler import config_reader, \
    del_section, \
    get_config_parser

app = Flask(__name__)
CORS(app)

PATH_INI = '/Users/alessandro.negrini/Desktop/config.ini'


@app.route('/conf', methods=["GET"])
def get_conf():
    """
    This API reads the configuration file and returns its value to the caller
    Returns:
        The conf values in a JSON format
    """
    return config_reader(get_config_parser(PATH_INI))


@app.route('/conf/<conf>', methods=["DELETE"])
def update_conf(conf):
    if del_section(get_config_parser(PATH_INI), PATH_INI, conf):
        return "True"
    else:
        return jsonify(isError=True,
                       message="Section has not been found in the config ini file or an error occurred during the new "
                               "config file ini saving.",
                       errorCode=500), 500


if __name__ == '__main__':
    app.run()
