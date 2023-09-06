import os

HOSTNAME_KEY="AMIANAPI_HOSTNAME"
PORT_KEY="AMIANAPI_PORT"
LOGGING_LEVEL_KEY="AMIANAPI_LOGGING_LEVEL"
INVENTORIES_PATH="AMIANAPI_INVENTORIES_PATH"

default_environment_variables = {
    HOSTNAME_KEY: "localhost",
    PORT_KEY: "8080",
    # TODO: See TODO Clean
    LOGGING_LEVEL_KEY: "10",
    INVENTORIES_PATH: "./tmp_inventories"
}

class Content():

    def get(key: str) -> str:
        '''Return 'key' environment variable value if defined,
        otherwise return the default value.'''
        return os.environ.get(key, default_environment_variables[key])