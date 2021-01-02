from src.parrocchie_valmalenco_be.utils.config_handler import get_config_parser, \
    config_reader, \
    section_present,\
    del_section

CONFIG_INI_PATH1 = 'test_files/test_config_static.ini'
CONFIG_INI_PATH2 = 'test_files/empty_config.ini'
CONFIG_INI_PATH3 = 'test_files/test_config_static_after_del.ini'


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


def test_config_reader():
    config1 = get_config_parser(CONFIG_INI_PATH1)
    config2 = get_config_parser(CONFIG_INI_PATH2)
    res1 = config_reader(config1)
    res2 = config_reader(config2)
    exp_dict = dict()
    exp_dict['lanzada'] = {'cam_ip': '192.168.1.2', 'cam_port': '200'}
    exp_dict['chiesa_vco'] = {'cam_ip': '192.168.1.1', 'cam_port': '200'}
    exp_dict['caspoggio'] = {'cam_ip': '192.168.1.3', 'cam_port': '200'}
    assert res1 == exp_dict
    assert res2 == dict()


def test_section_present():
    config1 = get_config_parser(CONFIG_INI_PATH1)
    config2 = get_config_parser(CONFIG_INI_PATH2)
    assert section_present(config1, 'caspoggio')
    assert section_present(config1, 'lanzada')
    assert section_present(config1, 'chiesa_vco')
    assert not section_present(config1, 'milano')
    assert not section_present(config2, 'caspoggio')


def test_del_section():
    config1 = get_config_parser(CONFIG_INI_PATH1)
    config2 = get_config_parser(CONFIG_INI_PATH2)
    del_section(config1, CONFIG_INI_PATH3, 'caspoggio')

    config3 = get_config_parser(CONFIG_INI_PATH3)
    assert len(config3.sections()) == 2
    assert 'caspoggio' not in config3.sections()
    assert 'lanzada' in config3.sections()

    del_section(config1, CONFIG_INI_PATH3, 'caspoggio')
    del_section(config1, CONFIG_INI_PATH3, 'chiesa_vco')
    del_section(config1, CONFIG_INI_PATH3, 'lanzada')
    config3 = get_config_parser(CONFIG_INI_PATH3)
    assert len(config3.sections()) == 0
    assert 'caspoggio' not in config3.sections()
    assert 'lanzada' not in config3.sections()
    assert 'chiesa_vco' not in config3.sections()

    res_f1 = del_section(config1, CONFIG_INI_PATH1, 'torre')
    res_f2 = del_section(config2, CONFIG_INI_PATH2, 'caspoggio')
    assert not res_f1
    assert not res_f2
