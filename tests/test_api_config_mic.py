from flask import Flask
import os
import json

from src.parrocchie_valmalenco_be.run import create_app
from src.parrocchie_valmalenco_be.utils.utils import get_env_var, set_env_var


def test_get_all_conf_GET():

    # temporary change the value of environment var, for testing purposes
    old_test_config = get_env_var('CONFIGINIPATH')
    set_env_var('CONFIGINIPATH', 'tests/test_files/test_config_static.ini')

    test_app = create_app()

    with test_app.test_client() as test_client:

        # TESTING THE 200 RESPONSE
        response = test_client.get('/confMic')
        assert response.status_code == 200

        json_res = json.loads(response.data)
        assert 'caspoggio' in json_res.keys()
        assert 'lanzada' in json_res.keys()
        assert 'chiesa_vco' in json_res.keys()
        assert 'spriana' not in json_res.keys()

        assert json_res['caspoggio']['cam_ip'] == "192.168.1.3"
        assert json_res['caspoggio']['cam_port'] == "200"
        assert json_res['lanzada']['cam_ip'] == "192.168.1.2"
        assert json_res['lanzada']['cam_port'] == "200"

    # recover old env var
    set_env_var('CONFIGINIPATH', old_test_config)


def test_del_or_get_conf_GET():

    # temporary change the value of environment var, for testing purposes
    old_test_config = get_env_var('CONFIGINIPATH')
    set_env_var('CONFIGINIPATH', 'tests/test_files/test_config_static.ini')

    test_app = create_app()

    with test_app.test_client() as test_client:

        # TESTING THE 200 RESPONSE
        response = test_client.get('/confMic/caspoggio')
        assert response.status_code == 200

        json_res = json.loads(response.data)
        assert 'caspoggio' in json_res.keys()
        assert json_res['caspoggio']['cam_ip'] == "192.168.1.3"
        assert json_res['caspoggio']['cam_port'] == "200"

        # TESTING THE 404 RESPONSE: section not found
        response = test_client.get('/confMic/spriana')
        assert response.status_code == 404
        json_res = json.loads(response.data)
        assert json_res['code'] == 404
        assert json_res['isError'] == True
        assert json_res['message'] == "Section has not been found in the config ini file"

    # recover old env var
    set_env_var('CONFIGINIPATH', old_test_config)


def test_del_or_get_conf_DELETE():
    # temporary change the value of environment var, for testing purposes
    old_test_config = get_env_var('CONFIGINIPATH')
    set_env_var('CONFIGINIPATH', 'tests/test_files/test_config_static.ini')

    test_app = create_app()
    with test_app.test_client() as test_client:

        # TESTING THE 404 RESPONSE: section not found
        response = test_client.delete('/confMic/spriana')
        assert response.status_code == 404
        json_res = json.loads(response.data)
        assert json_res['code'] == 404
        assert json_res['isError'] == True
        assert json_res['message'] == "Section has not been found in the config ini file"

        # TESTING THE 200 RESPONSE: deletion ok
        response = test_client.delete('/confMic/caspoggio')
        assert response.status_code == 200
        json_res = json.loads(response.data)
        assert json_res['code'] == 200
        assert json_res['isError'] == False
        assert json_res['message'] == "Section and its options has been successfully deleted"

        # Re-add the section just deleted
        from src.parrocchie_valmalenco_be.controllers.config_mic import add_section, get_config_parser
        from tests.test_config_mic import CONFIG_INI_PATH1
        resp = add_section(get_config_parser(CONFIG_INI_PATH1),
                           CONFIG_INI_PATH1, 'caspoggio', '192.168.1.3', 200)

    # recover old env var
    set_env_var('CONFIGINIPATH', old_test_config)


def test_del_or_get_conf_PUT():
    # temporary change the value of environment var, for testing purposes
    old_test_config = get_env_var('CONFIGINIPATH')
    set_env_var('CONFIGINIPATH', 'tests/test_files/test_config_static.ini')

    test_app = create_app()
    with test_app.test_client() as test_client:

        # TESTING THE 404 RESPONSE: section not found
        response = test_client.put('/confMic/spriana', data=json.dumps(dict(
            cam_ip="192.168.1.99",
            cam_port="400")),
            content_type='application/json')
        assert response.status_code == 404
        json_res = json.loads(response.data)
        assert json_res['code'] == 404
        assert json_res['isError'] == True
        assert json_res['message'] == "Section has not been found in the config ini file"

        # TESTING THE 200 RESPONSE: update ok
        response = test_client.put('/confMic/caspoggio', data=json.dumps(dict(
            cam_ip="192.168.1.99",
            cam_port="199")),
            content_type='application/json')
        assert response.status_code == 200
        json_res = json.loads(response.data)
        assert json_res['code'] == 200
        assert json_res['isError'] == False
        assert json_res['message'] == "Section has been successfully updated"

        # Recover the section just modified
        from src.parrocchie_valmalenco_be.controllers.config_mic import update_section, get_config_parser
        from tests.test_config_mic import CONFIG_INI_PATH1
        resp = update_section(get_config_parser(CONFIG_INI_PATH1),
                              CONFIG_INI_PATH1, 'caspoggio', {'cam_ip': '192.168.1.3', 'cam_port': '200'})

    # recover old env var
    set_env_var('CONFIGINIPATH', old_test_config)


def test_add_conf_POST():
    # temporary change the value of environment var, for testing purposes
    old_test_config = get_env_var('CONFIGINIPATH')
    set_env_var('CONFIGINIPATH', 'tests/test_files/test_config_static.ini')

    test_app = create_app()
    with test_app.test_client() as test_client:

        # TESTING THE 409 RESPONSE
        response = test_client.post('/confMic', data=json.dumps(dict(
            key="caspoggio",
            cam_ip="192.168.1.100",
            cam_port=200)),
            content_type='application/json')
        assert response.status_code == 409
        json_res = json.loads(response.data)
        assert json_res['code'] == 409
        assert json_res['isError'] == True
        assert json_res['message'] == "A section with that key is already present. Consider to use the specific endpoint for its modication"

        # TESTING THE 201 RESPONSE
        response = test_client.post('/confMic', data=json.dumps(dict(
            key="spriana",
            cam_ip="192.168.1.100",
            cam_port=200)),
            content_type='application/json')
        assert response.status_code == 201
        json_res = json.loads(response.data)
        assert json_res['code'] == 201
        assert json_res['isError'] == False
        assert json_res['message'] == "Section and its options has been successfully created"

        # Delete the section just added
        from src.parrocchie_valmalenco_be.controllers.config_mic import del_section, get_config_parser
        from tests.test_config_mic import CONFIG_INI_PATH1
        resp = del_section(get_config_parser(
            CONFIG_INI_PATH1), CONFIG_INI_PATH1, 'spriana')

    # recover old env var
    set_env_var('CONFIGINIPATH', old_test_config)
