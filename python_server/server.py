import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Type
import uuid

class SimpleRequestHandler(BaseHTTPRequestHandler):
    user_list = [
        {'uuid': str(uuid.uuid4()), 
         'first_name': 'Kasia', 
         'last_name': 'Topor', 
         'role': 'Student'}
    ]

    def do_OPTIONS(self):
        self.send_response(200, "OK")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        self.wfile.write(json.dumps(SimpleRequestHandler.user_list).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        new_member = json.loads(post_data.decode())
        new_member['uuid'] = str(uuid.uuid4())
        SimpleRequestHandler.user_list.append(new_member)  

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        self.wfile.write(json.dumps(SimpleRequestHandler.user_list).encode())

    def do_DELETE(self):
        path_parts = self.path.split('/')
        user_uuid = path_parts[-1] 
        
        SimpleRequestHandler.user_list = [
            user for user in SimpleRequestHandler.user_list if user['uuid'] != user_uuid
        ]
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "User deleted", "updated_list": SimpleRequestHandler.user_list}).encode())

def run(server_class: Type[HTTPServer] = HTTPServer, handler_class: Type[BaseHTTPRequestHandler] = SimpleRequestHandler, port: int = 8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
