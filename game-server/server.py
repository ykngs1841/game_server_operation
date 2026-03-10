from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import Counter, generate_latest

REQUEST_COUNT = Counter("game_requests_total", "Total Game Requests")

class GameHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(generate_latest())

        else:
            REQUEST_COUNT.inc()
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", 8080), GameHandler)

print("Game Server running on port 8080")

server.serve_forever()