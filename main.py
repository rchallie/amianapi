# TODO 11: TUI: List project and url as a navlist tree on left
# TODO 12: TUI: Url editor

# TODO Backlog:
# - routes_list => Projects Navigation
# - Project Create:
#   - Error messages:
#       - Project name already exists
#       - Empty Project name
# - Stop server when close TUI
# - A route can only be saved if another route with same path avec different trigger conditions (so add trigger condition)
# - Add Request type handle - GET
# - Url list in a project (route list as tree)
# - Activate / deactivate a route
# - give an array of every field as param to route_inv functions with a checker
# - Each route must be identified with a UUID not by path (Allow multiple définition for a same route (if own route is set as on, another routes are set to off))
# - Dynamic route with params that can be used in reply (like /plop/:id => Reply: your id is :id)
# - Fast exec, just give the json config file as path and deserv defined paths
# - Shared inventory between users
# - Function to manage routes as API (Allow to create own external (T)UI)
# - Handle requests as thread

# TODO To be clean:
# - LOGGING_LEVEL as env var + correspondance table between our and logging variable type
# - Comments

import logging

import sources.environment as Environment

from sources.tui.app import TUI
from sources.server.threaded_httpd import ThreadedHTTPd

# VERY TEMPORARY
import os
os.remove("amianapi.log")
logging.basicConfig(filename="amianapi.log", filemode='a', format='[%(threadName)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=int(Environment.Content.get(Environment.LOGGING_LEVEL_KEY)))

if __name__ == '__main__':

    httpd_thread = ThreadedHTTPd(name="httpd_thread")
    httpd_thread.start()

    app = TUI()
    app.run()
