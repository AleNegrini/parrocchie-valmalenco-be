from flask import request, jsonify, Blueprint

from src.parrocchie_valmalenco_be.controllers.config_mic import \
    get_all_sections, \
    del_section, \
    get_config_parser,\
    get_section,\
    add_section,\
    update_section
from src.parrocchie_valmalenco_be.utils.config import MIC_CONFIG_PATH_INI

# define config_handler blueprint
configMic_blueprint = Blueprint('confMic', __name__,)


@configMic_blueprint.route('/confMic', methods=["GET"])
def get_all_conf():
    """
    This API reads the configuration file and returns its value to the caller
    Returns:
        The conf values in a JSON format
    """
    return get_all_sections(get_config_parser(MIC_CONFIG_PATH_INI))


@configMic_blueprint.route('/confMic', methods=['POST'])
def add_conf():
    body_request = request.get_json()
    key = body_request['key']
    opt1 = body_request['cam_ip']
    opt2 = body_request['cam_port']
    if add_section(config=get_config_parser(path=MIC_CONFIG_PATH_INI), path=MIC_CONFIG_PATH_INI, key=key, opt1=opt1, opt2=opt2) == 0:
        return jsonify(isError=False,
                       message="Section and its options has been successfully created",
                       code=201), 201
    if add_section(config=get_config_parser(path=MIC_CONFIG_PATH_INI), path=MIC_CONFIG_PATH_INI, key=key, opt1=opt1, opt2=opt2) == 1:
        return jsonify(isError=True,
                       message="A section with that key is already present",
                       code=409), 409
    if add_section(config=get_config_parser(path=MIC_CONFIG_PATH_INI), path=MIC_CONFIG_PATH_INI, key=key, opt1=opt1, opt2=opt2) == 2:
        return jsonify(isError=True,
                       message="An error occurred while saving the section and the options",
                       code=500), 500
    else:
        return jsonify(isError=True,
                       message="An unexpected error occurred",
                       code=500), 500


@configMic_blueprint.route('/confMic/<conf>', methods=["GET", "DELETE", "PUT"])
def del_or_get_conf(conf):
    if request.method == 'GET':
        resp = get_section(config=get_config_parser(
            path=MIC_CONFIG_PATH_INI), key=conf)
        if resp is None:
            return jsonify(isError=True,
                           message="Section has not been found in the config ini file",
                           code=404), 404
        else:
            return resp

    if request.method == 'DELETE':
        if del_section(config=get_config_parser(path=MIC_CONFIG_PATH_INI), path=MIC_CONFIG_PATH_INI, key=conf) == 0:
            return jsonify(isError=False,
                           message="Section and its options has been successfully deleted",
                           code=200), 200
        if del_section(config=get_config_parser(path=MIC_CONFIG_PATH_INI), path=MIC_CONFIG_PATH_INI, key=conf) == 1:
            return jsonify(isError=True,
                           message="Section has not been found in the config file",
                           code=404), 404
        if del_section(config=get_config_parser(path=MIC_CONFIG_PATH_INI), path=MIC_CONFIG_PATH_INI, key=conf) == 2:
            return jsonify(isError=True,
                           message="An error occurred while saving the section and the options",
                           code=500), 500
        else:
            return jsonify(isError=True,
                           message="An unexpected error occurred",
                           code=500), 500
    else:
        body_request = request.get_json()

        if update_section(config=get_config_parser(path=MIC_CONFIG_PATH_INI), path=MIC_CONFIG_PATH_INI, key=conf, obj=body_request) == 0:
            return jsonify(isError=False,
                           message="Section has been successfully updated",
                           code=200), 200
        if update_section(config=get_config_parser(path=MIC_CONFIG_PATH_INI), path=MIC_CONFIG_PATH_INI, key=conf, obj=body_request) == 1:
            return jsonify(isError=True,
                           message="Section has not been found in the config file",
                           code=404), 404
        if update_section(config=get_config_parser(path=MIC_CONFIG_PATH_INI), path=MIC_CONFIG_PATH_INI, key=conf, obj=body_request) == 1:
            return jsonify(isError=True,
                           message="An error occurred while saving the section and the options",
                           code=500), 500
        else:
            return jsonify(isError=True,
                           message="An unexpected error occurred",
                           code=500), 500
