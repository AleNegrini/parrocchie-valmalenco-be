import configparser


def section_present(config, key):
    """
    It indicates whether the key section is present in the config file
    Args:
        config: config parser object
        key: section key

    Returns:
        True if the section is present, False elsewhere
    """
    keys = config.sections()
    if key in keys:
        return True
    else:
        return False


def get_section(config, key):
    """
    It gets the options of the specified section (if present). Otherwise None is returned
    Args:
        config: config parser object
        key: section key

    Returns:
        The section and its options as object.
        None if the section is not present
    """
    if not section_present(config, key):
        return None
    else:
        rdict = dict()
        rdict[key] = {'cam_ip': config.get(key, 'cam_ip'), 'cam_port': config.get(key, 'cam_port')}
        return rdict


def del_section(config, path, key):
    """
    It deletes the section and the respective attributes from the config.ini file
    Args:
        config: config parser object
        path: config file path where to save the new config file
        key: section key

    Returns:
        True if the delete operation run successfully, False elsewhere

    """

    if section_present(config, key):

        # deleting the four options for the specific key
        config.remove_option(key, 'cam_ip')
        config.remove_option(key, 'cam_port')
        config.remove_option(key, 'username')
        config.remove_option(key, 'password')
        config.remove_section(key)

        # save the new config to the config ini file
        try:
            with open(path, 'w+') as conf:
                config.write(conf)
                return True
        except IOError as e:
            print("An error occurred while saving config to file: "+str(e))
            return False
    else:
        print("No section available in the config file")
        return False


def add_section(config, path, key, opt1, opt2):
    """
    It add a new section and the respective attributes to the config.ini file
    Args:
        config: config parser object
        path: config file path where to save the new config file
        key: config object key section
        opt1: config object option 'cam_ip'
        opt2: config object option 'cam_port'

    Returns:
        0: if the section is correctly added
        1: if the section is already present
        2: if an error occurs during the file write

    """

    obj_conf = configparser.ConfigParser()
    obj_conf[key] = {'cam_ip': opt1, 'cam_port': opt2}

    if section_present(config, key):
        return 1
    else:
        try:
            with open(path, 'a') as conf:
                obj_conf.write(conf)
                return 0
        except IOError as e:
            print("An error occurred while saving config to file: " + str(e))
            return 2


def get_all_sections(config):
    """
    It reads the config file and returns its content as a dictionary
    Args:
        config: config parser object
    Returns:
        config file content

    """

    conf_dict = dict()

    # get all the ini sections
    keys = config.sections()

    # build the dictionary
    for key in keys:
        conf_dict[key] = {
            'cam_ip': config[key]['cam_ip'],
            'cam_port': config[key]['cam_port']
        }

    return conf_dict


def get_config_parser(path):
    """It prepares and returns the ConfigParser object
    Args:
        path: config file path

    Returns:
        ConfigParser object in that path
    """
    config = configparser.ConfigParser()
    config.read(path)
    return config

