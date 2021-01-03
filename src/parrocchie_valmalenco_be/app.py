from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

from src.parrocchie_valmalenco_be.utils.config_handler import \
    get_all_sections, \
    del_section, \
    get_config_parser,\
    get_section,\
    add_section

app = Flask(__name__)
CORS(app)

PATH_INI = '/Users/alessandro.negrini/Desktop/config.ini' # da sistemare


@app.route('/conf', methods=["GET"])
def get_all_conf():
    """
    This API reads the configuration file and returns its value to the caller
    Returns:
        The conf values in a JSON format
    """
    return get_all_sections(get_config_parser(PATH_INI))


@app.route('/conf/<conf>', methods=["GET", "DELETE"])
def del_or_get_conf(conf):
    if request.method == 'GET':
        resp = get_section(config=get_config_parser(path=PATH_INI), key=conf)
        if resp is None:
            return jsonify(isError=True,
                           message="Section has not been found in the config ini file",
                           errorCode=404), 404
        else:
            return resp

    else:
        if del_section(config=get_config_parser(path=PATH_INI), path=PATH_INI, key=conf) == 0:
            return jsonify(isError=False,
                           message="Section and its options has been successfully deleted",
                           errorCode=200), 200
        if del_section(config=get_config_parser(path=PATH_INI), path=PATH_INI, key=conf) == 1:
            return jsonify(isError=True,
                           message="Section has not been found in the config file",
                           errorCode=404), 404
        if del_section(config=get_config_parser(path=PATH_INI), path=PATH_INI, key=conf) == 2:
            return jsonify(isError=True,
                           message="An error occurred while saving the section and the options",
                           errorCode=500), 500
        else:
            return jsonify(isError=True,
                           message="An unexpected error occurred",
                           errorCode=500), 500


@app.route('/conf', methods=['POST'])
def add_conf():
    body_request = request.get_json()
    key = body_request['key']
    opt1 = body_request['cam_ip']
    opt2 = body_request['cam_port']
    if add_section(config=get_config_parser(path=PATH_INI), path=PATH_INI, key=key, opt1=opt1, opt2=opt2) == 0:
        return jsonify(isError=False,
                       message="Section and its options has been successfully created"), 201
    if add_section(config=get_config_parser(path=PATH_INI), path=PATH_INI, key=key, opt1=opt1, opt2=opt2) == 1:
        return jsonify(isError=True,
                       message="A section with that key is already present",
                       errorCode=409), 409
    if add_section(config=get_config_parser(path=PATH_INI), path=PATH_INI, key=key, opt1=opt1, opt2=opt2) == 2:
        return jsonify(isError=True,
                       message="An error occurred while saving the section and the options",
                       errorCode=500), 500
    else:
        return jsonify(isError=True,
                       message="An unexpected error occurred",
                       errorCode=500), 500


if __name__ == '__main__':
    app.run()
