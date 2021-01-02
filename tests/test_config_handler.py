import pytest
from src.parrocchie_valmalenco_be.utils.config_handler import get_config_parser

CONFIG_INI_PATH1 = 'test_files/test_config_static.ini'
CONFIG_INI_PATH2 = 'test_files/empty_config.ini'


def test_get_config_parser_len():
    config = get_config_parser(CONFIG_INI_PATH1)
    assert len(config.sections()) == 3
    config = get_config_parser(CONFIG_INI_PATH2)
    assert len(config.sections()) == 0


def test_get_config_parser_sections():
    config = get_config_parser(CONFIG_INI_PATH1)
    assert 'caspoggio' in config.sections()
    assert 'chiesa_vco' in config.sections()
    assert 'lanzada' in config.sections()


def test_get_config_parser_option():
    config = get_config_parser(CONFIG_INI_PATH1)
    assert config.get('caspoggio', 'cam_ip') == "192.168.1.3"


