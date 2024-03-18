import socket

def main():
    HOST = '127.0.0.1'
    PORT = 2010

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print("Serwer oczekuje na połączenie...")

        conn, addr = server_socket.accept()
        print("Połączono z klientem:", addr)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Otrzymane dane od klienta:", data.decode())
            conn.sendall(data)

    except Exception as e:
        print("Wystąpił błąd:", e)

    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    main()
