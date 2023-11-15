import http.server
import socketserver
import os

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Respond to a GET request.
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()

            # Print environment variables
            self.wfile.write(b"Environment Variables:\n")
            for key, value in os.environ.items():
                self.wfile.write(f"{key}: {value}\n".encode())

            # Print properties from the properties file
            self.wfile.write(b"\nProperties from /etc/app/properties.txt:\n")
            try:
                with open('/etc/app/properties.txt', 'r') as f:
                    for line in f:
                        self.wfile.write(f"{line}".encode())
            except FileNotFoundError:
                self.wfile.write(b"Properties file not found.\n")
            except Exception as e:
                self.wfile.write(f"An error occurred: {e}\n".encode())

        else:
            self.send_error(404, "File not found")

# Set up HTTP server and socket
handler_object = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print(f"Server started at localhost:{PORT}")
    httpd.serve_forever()
