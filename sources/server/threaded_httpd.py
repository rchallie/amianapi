import logging

import sources.environment as Environment

from threading import Thread
from http.server import HTTPServer

from .server import Server

class ThreadedHTTPd(Thread):

    def run(self) -> None:

        server_hostname = Environment.Content.get(Environment.HOSTNAME_KEY)
        server_port = int(Environment.Content.get(Environment.PORT_KEY))

        # Configure HTTP Server
        httpd = HTTPServer((server_hostname, server_port), Server)
        logging.info(f"Server UP - {server_hostname}:{server_port}'")

        # Open HTTP Server
        httpd.serve_forever()

        # Close HTTP Server
        httpd.server_close()
        logging.info(f"Server DOWN - {server_hostname}:{server_port}'")