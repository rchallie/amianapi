# TODO 1: Create web Server that reply "Hello World!"
# TODO 2: Get web server routes and replies from dict (router)
# TODO 3: Get web server routes and reploies from inventory file
# TODO 4: Add route and reply from inventory file
# TODO 5: Remove route and reply from inventory file
# TODO 6: Update route and reply from inventory file
# TODO 7: Add Status code definition
# TODO 8: Add Request type handle - GET 
# TODO 9: Url list in a project
# TODO 10: Webserver as a thread
# TODO 11: TUI: List project and url as a navlist tree on left
# TODO 12: TUI: Url editor

# TODO Backlog:
# - Dynamic route with params that can be used in reply (like /plop/:id => Reply: your id is :id)

# TODO To be clean:
# - HOST_NAME and PORT_NUMBER as env vars
# - LOGGING_LEVEL as env var + correspondance table between our and logging variable type
# - Comments

import logging

import sources.environment as Environment

from http.server import HTTPServer

from sources.server.server import Server

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=int(Environment.Content.get(Environment.ENV_VAR_LOGGING_LEVEL_KEY)))

if __name__ == '__main__':

    server_hostname = Environment.Content.get(Environment.ENV_VAR_HOSTNAME_KEY)
    server_port = int(Environment.Content.get(Environment.ENV_VAR_PORT_KEY))

    # Configure HTTP Server
    httpd = HTTPServer((server_hostname, server_port), Server)
    logging.info(f"Server UP - {server_hostname}:{server_port}'")

    # Open HTTP Server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    # Close HTTP Server
    httpd.server_close()
    logging.info(f"Server DOWN - {server_hostname}:{server_port}'")
    