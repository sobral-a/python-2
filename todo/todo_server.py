import http.server
import json
from . import db

HTTP_PORT = 8000
HOST_NAME = '127.0.0.1'

class CustomHandler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', ' GET,POST,PATCH,DELETE')
    self.send_header('Content-Type', 'application/json;')
    self.end_headers()
    body = json.dumps(db.find())
    self.wfile.write(body.encode('utf-8'))
  
  def do_POST(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', ' GET,POST,PATCH,DELETE')
    self.end_headers()
    body_length = int(self.headers['Content-Length'])
    post_body = self.rfile.read(body_length)
    db.create(post_body.decode('utf-8'))
  
  def do_PATCH(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', ' GET,POST,PATCH,DELETE')
    self.end_headers()
    db.toggle(self.path[1:])
  
  def do_DELETE(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', ' GET,POST,PATCH,DELETE')
    self.end_headers()
    db.remove(self.path[1:])


class TodoServer:
  def __init__(self):
    self.server = http.server.HTTPServer((HOST_NAME, HTTP_PORT), CustomHandler)

  def run(self):
    self.server.serve_forever()
