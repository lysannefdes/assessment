from http.server import BaseHTTPRequestHandler, HTTPServer
import time

host = "0.0.0.0"
port = 8080


class simpleServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1> HELLO WORLD! </h1></body></html>", "utf-8"))
        self.wfile.write()
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1> THIS IS RESPONSE TO POST REQUEST </h1></body></html>", "utf-8"))

server = HTTPServer((host, port), simpleServer)
print("Server is now running ...")
server.serve_forever()
server.server_close()

print("Sever stopped")
