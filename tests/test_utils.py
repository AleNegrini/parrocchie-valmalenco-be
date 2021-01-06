import os
import pytest
from src.parrocchie_valmalenco_be.utils.utils import get_env_var, set_env_var


def test_get_env_var():
    os.environ["KEY"] = "Test"
    assert get_env_var("KEY") == "Test"
    with pytest.raises(KeyError):
        get_env_var("MISSING KEY")


def test_set_env_var():
    set_env_var("TEST_KEY", "1")
    assert get_env_var("TEST_KEY") == "1"
    set_env_var("TEST_KEY", "")
    assert get_env_var("TEST_KEY") == ""
