import socket

def main():
    HOST = '127.0.0.1'
    PORT = 2010

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        print("Połączono z serwerem echa.")

        message = input("Wprowadź wiadomość do wysłania: ")

        client_socket.sendall(message.encode())
        print("Wysłano wiadomość:", message)

        response = client_socket.recv(1024)
        print("Otrzymano odpowiedź od serwera:", response.decode())

    except Exception as e:
        print("Wystąpił błąd:", e)

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
