from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

def run_server():
    server_address = ('', 4443)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   certfile='./server.pem',
                                   keyfile='./server.key',
                                   ssl_version=ssl.PROTOCOL_TLS)

    print("Serwer HTTPS działa na porcie 4443")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
