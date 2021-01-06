import os


def get_env_var(var):
    """
    It gets the value of the specified env. variable and it returns it 
    Args:
        var: environment variable name

    Returns:
        The environment variable content (f present). Otherwise a KeyError is raised
    """
    try:
        return os.environ[var]
    except KeyError as err:
        print("An error occurred during env variable reading. "+str(err))
        raise KeyError(err)


def set_env_var(var, val):
    """
    It sets the value of the specified env. variable with value 'val'
    Args:
        var: environment variable name
        val: environment variable value
    """
    os.environ[var] = val
