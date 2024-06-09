import socket
import ssl


def echo_server():
    HOST = '127.0.0.1'
    PORT = 12345
    CERTFILE = './server.pem'
    KEYFILE = './server.key'

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"Serwer nasłuchuje na {HOST}:{PORT}")

    while True:
        client_sock, addr = sock.accept()
        secure_sock = context.wrap_socket(client_sock, server_side=True)
        print(f"Połączenie z {addr}")

        try:
            while True:
                data = secure_sock.recv(4096)
                if not data:
                    break
                secure_sock.sendall(data)
        except Exception as e:
            print(f"Błąd: {e}")
        finally:
            secure_sock.close()


if __name__ == '__main__':
    echo_server()
