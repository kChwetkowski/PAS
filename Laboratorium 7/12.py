import socket

POP3_SERVER_ADDRESS = "127.0.0.1"
POP3_SERVER_PORT = 1100

MESSAGES = [
    b"From: sender@example.com\r\nTo: receiver@example.com\r\nSubject: Test message\r\n\r\nThis is a test message.\r\n",
    b"From: sender@example.com\r\nTo: receiver@example.com\r\nSubject: Another message\r\n\r\nThis is another test message.\r\n",
]


USERS = {
    "Steve": "Fox",
}

def handle_client_connection(client_socket):
    client_socket.send(b"+OK POP3 server ready\r\n")

    is_authenticated = False
    current_user = None

    while True:
        request = client_socket.recv(1024)

        if not request:
            break

        if request.startswith(b"USER"):
            username = request.split(b" ")[1].strip().decode()
            if username in USERS:
                client_socket.send(b"+OK User recognized\r\n")
                current_user = username
            else:
                client_socket.send(b"-ERR User not recognized\r\n")

        elif request.startswith(b"PASS"):
            if current_user is None:
                client_socket.send(b"-ERR Must specify USER first\r\n")
            else:
                password = request.split(b" ")[1].strip().decode()
                if USERS.get(current_user) == password:
                    client_socket.send(b"+OK User successfully logged in\r\n")
                    is_authenticated = True
                else:
                    client_socket.send(b"-ERR Incorrect password\r\n")

        elif is_authenticated:
            if request.startswith(b"STAT"):
                total_messages = len(MESSAGES)
                total_bytes = sum(len(msg) for msg in MESSAGES)
                response = f"+OK {total_messages} {total_bytes}\r\n"
                client_socket.send(response.encode())

            elif request.startswith(b"LIST"):
                response = "+OK\r\n"
                for i, msg in enumerate(MESSAGES, start=1):
                    msg_size = len(msg)
                    response += f"{i} {msg_size}\r\n"
                response += ".\r\n"
                client_socket.send(response.encode())


            elif request.startswith(b"RETR"):
                try:
                    parts = request.split()
                    if len(parts) < 2:
                        raise ValueError("No message number provided")
                    msg_num = int(parts[1])

                    if 1 <= msg_num <= len(MESSAGES):
                        msg = MESSAGES[msg_num - 1]
                        client_socket.send(b"+OK\r\n")
                        client_socket.send(msg)
                        client_socket.send(b".\r\n")

                    else:
                        client_socket.send(b"-ERR Message does not exist\r\n")

                except ValueError as e:
                    client_socket.send(b"-ERR " + str(e).encode() + b"\r\n")


            elif request.startswith(b"QUIT"):
                client_socket.send(b"+OK Bye\r\n")
                break

            else:
                client_socket.send(b"-ERR Command not implemented\r\n")

        else:
            client_socket.send(b"-ERR Must authenticate first\r\n")

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((POP3_SERVER_ADDRESS, POP3_SERVER_PORT))
    server_socket.listen(5)
    print(f"Listening for incoming connections on {POP3_SERVER_ADDRESS}:{POP3_SERVER_PORT}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
            handle_client_connection(client_socket)

    except KeyboardInterrupt:
        print("Server stopped")

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
