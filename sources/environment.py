import os

ENV_VAR_HOSTNAME_KEY="AMIANAPI_HOSTNAME"
ENV_VAR_PORT_KEY="AMIANAPI_PORT"
ENV_VAR_LOGGING_LEVEL_KEY="AMIANAPI_LOGGING_LEVEL"

default_environment_variables = {
    ENV_VAR_HOSTNAME_KEY: "localhost",
    ENV_VAR_PORT_KEY: "8080",
    # TODO: See TODO Clean
    ENV_VAR_LOGGING_LEVEL_KEY: "10"
}

class Content():

    def get(key: str) -> str:
        '''Return 'key' environment variable value if defined,
        otherwise return the default value.'''
        return os.environ.get(key, default_environment_variables[key])