import socket

def main():
    HOST = '127.0.0.1'
    PORT = 2010

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        message = "Hello, server!"
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024).decode()
        print("Odpowiedź od serwera:", response)
        
    except Exception as e:
        print("Wystąpił błąd:", e)

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
