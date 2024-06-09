import socket
import ssl


def tcp_client():
    HOST = '212.182.24.27'
    PORT = 29443

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
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
    tcp_client()
