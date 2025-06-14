#!/usr/bin/env python3
import http.server
import socketserver
import json

PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_header("Content-Type", "application/json")

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"name":"John","age":30,"city":"New York"}')

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"OK"}')

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error":"Endpoint not found"}')

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Serving on http://localhost:{PORT}")
        httpd.serve_forever()
