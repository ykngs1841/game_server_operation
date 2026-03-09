from http.server import BaseHTTPRequestHandler, HTTPServer

class GameHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", 8080), GameHandler)

print("Game Server running on port 8080")

server.serve_forever()