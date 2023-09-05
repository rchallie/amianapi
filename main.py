# TODO 10: Webserver as a thread
# TODO 11: TUI: List project and url as a navlist tree on left
# TODO 12: TUI: Url editor

# TODO Backlog:
# - Add Request type handle - GET
# - Url list in a project
# - Activate / deactivate a route
# - give an array of every field as param to route_inv functions with a checker
# - Each route must be identified with a UUID not by path (Allow multiple définition for a same route (if own route is set as on, another routes are set to off))
# - Dynamic route with params that can be used in reply (like /plop/:id => Reply: your id is :id)
# - Fast exec, just give the json config file as path and deserv defined paths
# - Shared inventory between users

# TODO To be clean:
# - LOGGING_LEVEL as env var + correspondance table between our and logging variable type
# - Comments

import logging

import sources.environment as Environment

from http.server import HTTPServer

from sources.server.server import Server

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=int(Environment.Content.get(Environment.LOGGING_LEVEL_KEY)))

if __name__ == '__main__':

    server_hostname = Environment.Content.get(Environment.HOSTNAME_KEY)
    server_port = int(Environment.Content.get(Environment.PORT_KEY))

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
    