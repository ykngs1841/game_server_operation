from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

server = HTTPServer(("0.0.0.0", 8080), HealthHandler)
print("Server running on port 8080")
server.serve_forever()
