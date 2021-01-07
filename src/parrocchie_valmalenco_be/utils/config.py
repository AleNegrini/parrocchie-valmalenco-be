from src.parrocchie_valmalenco_be.utils.utils import get_env_var

# production use config
MIC_CONFIG_PATH_INI = get_env_var('CONFIGINIPATH')

# API response codes
SUCCESS_CODE = 200
CREATED_CODE = 201
NOT_FOUND_CODE = 404
IS_ERROR_CODE = 500
CONFLICT_CODE = 409

# API response strings
SUCCESS_ADD_MESSAGE = "Section and its options has been successfully created"
SUCCESS_DEL_MESSAGE = "Section and its options has been successfully deleted"
SUCCESS_UPD_MESSAGE = "Section has been successfully updated"
FILEW_ERROR_MESSAGE = "An error occurred while saving the section and the options"
UNEXP_ERROR_MESSAGE = "An unexpected error occurred"
CONFLICT_SECT_MESSAGE = "A section with that key is already present. Consider to use the specific endpoint for its modication"
NOT_FOUND_MESSAGE = "Section has not been found in the config ini file"
