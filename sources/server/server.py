import logging

from .router import Router

from http.server import BaseHTTPRequestHandler

router = Router()
router.add_route("/plop", "Add meh", 200, "text/plain")

class Server(BaseHTTPRequestHandler):

  def do_GET(self) -> None:
    self.respond()

  def handle_http(self) -> bytes:

    if router.has_route(self.path):

      # Get route informations
      route_response = router.get_route(self.path)
      status_code = route_response["status_code"]
      content_type = route_response["content_type"]
      response_body = route_response["body"]

    # Route not found
    else:

      status_code = 404
      content_type = "text/plain"
      response_body = "404 Not Found"


    # HTTP response header generation
    self.send_response(status_code)
    self.send_header('Content-type', content_type)
    self.end_headers()
    
    # HTTP response body generation
    return bytes(response_body, "UTF-8")

  def respond(self) -> None:
    
    # HTTP response generation
    content = self.handle_http()
    self.wfile.write(content)