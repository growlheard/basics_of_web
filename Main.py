import json
from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localHost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        responce = 'Hello, World wide web!'
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(responce, 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"Полученные данные POST-запроса: {post_data}")
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(f"Данные:( {post_data} )успешно добавлены!", 'utf-8'))


if __name__ == '__main__':
    server_address = (hostName, serverPort)
    httpd = HTTPServer(server_address, MyServer)
    print(f"Сервер запущен на  http://{hostName}:{serverPort}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Сервер остановлен')
