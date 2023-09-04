from http.server import BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):

  def do_GET(self):
    self.respond()

  def handle_http(self, status, content_type):

    # HTTP response header generation
    self.send_response(status)
    self.send_header('Content-type', content_type)
    self.end_headers()

    # HTTP response body generation
    return bytes("Hello World!", "UTF-8")
    
  def respond(self):
    
    # HTTP response generation
    content = self.handle_http(200, 'text/html')
    self.wfile.write(content)