import os

HOSTNAME_KEY="AMIANAPI_HOSTNAME"
PORT_KEY="AMIANAPI_PORT"
LOGGING_LEVEL_KEY="AMIANAPI_LOGGING_LEVEL"
INVENTORY_PATH="AMIANAPI_INVENTORY_PATH"

default_environment_variables = {
    HOSTNAME_KEY: "localhost",
    PORT_KEY: "8080",
    # TODO: See TODO Clean
    LOGGING_LEVEL_KEY: "10",
    INVENTORY_PATH: "./tmp_inventory.json"
}

class Content():

    def get(key: str) -> str:
        '''Return 'key' environment variable value if defined,
        otherwise return the default value.'''
        return os.environ.get(key, default_environment_variables[key])