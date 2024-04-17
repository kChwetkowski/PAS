import socket
import base64

# Adres i port serwera SMTP
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 2500

# Dane do uwierzytelnienia
USERNAME = 'testuser'
PASSWORD = 'testpassword'


def base64_encode(data):
    return base64.b64encode(data.encode()).decode()


def base64_decode(data):
    return base64.b64decode(data).decode()

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.send(b'EHLO localhost\r\n')
    response = client_socket.recv(1024).decode()
    print(response)

    if 'AUTH' in response:
        client_socket.send(b'AUTH LOGIN\r\n')
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.send(base64_encode(USERNAME) + b'\r\n')
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.send(base64_encode(PASSWORD) + b'\r\n')
        response = client_socket.recv(1024).decode()
        print(response)

    client_socket.send(b'MAIL FROM: <sender@example.com>\r\n')
    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.send(b'RCPT TO: <recipient@example.com>\r\n')
    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.send(b'DATA\r\n')
    response = client_socket.recv(1024).decode()
    print(response)

    message = """\
From: <sender@example.com>
To: <recipient@example.com>
Subject: Test Email.

Test mail.
"""
    client_socket.send(message.encode() + b'\r\n')
    client_socket.send(b'.\r\n')
    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.send(b'QUIT\r\n')
    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()


if __name__ == "__main__":
    main()
