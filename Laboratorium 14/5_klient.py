import socket
import ssl


def echo_client():
    HOST = '127.0.0.1'
    PORT = 12345
    CA_CERT = './server.pem'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations(CA_CERT)

    secure_sock = context.wrap_socket(sock, server_hostname=HOST)

    while True:
        message = input("Podaj wiadomość do wysłania: ")
        if message.lower() == 'exit':
            break
        secure_sock.sendall(message.encode())
        response = secure_sock.recv(4096)
        print("Odpowiedź z serwera:", response.decode())

    secure_sock.close()
    sock.close()


if __name__ == '__main__':
    echo_client()
