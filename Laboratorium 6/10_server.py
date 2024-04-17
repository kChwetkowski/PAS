import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 2500

# 220: Serwer gotowy, powitanie
# 250: Sukces, komenda została wykonana pomyślnie
# 354: Wysyłanie danych (np. treści wiadomości)
# 500: Błąd składni, nieznana komenda
# 221: Zakończenie połączenia

def handle_client_connection(client_socket):
    # Powitanie
    client_socket.send(b'220 localhost: Serwer SMTP gotowy\r\n')

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        # dane do tekstu
        command = data.decode().strip().upper()

        #HELO/EHLO
        if command.startswith('HELO') or command.startswith('EHLO'):
            client_socket.send(b'250 localhost\r\n')

        #MAIL FROM
        elif command.startswith('MAIL FROM:'):
            client_socket.send(b'250 OK\r\n')

        #RCPT TO
        elif command.startswith('RCPT TO:'):
            client_socket.send(b'250 OK\r\n')

        #DATA
        elif command == 'DATA':
            client_socket.send(b'354 Poczatek wiadomosci; zakoncz <CRLF>.<CRLF>\r\n')
            message_data = b''
            while True:
                line = client_socket.recv(1024)
                if line.strip() == b'.':
                    break
                message_data += line
            client_socket.send(b'250 OK\r\n')

        elif command == 'QUIT':
            client_socket.send(b'221 localhost: zamykanie polaczenia\r\n')
            break

        else:
            client_socket.send(b'500 Blad skladni, nieznana komenda\r\n')

    client_socket.close()



def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"[*] Nasłuchiwanie na przychodzące połączenia na {SERVER_HOST}:{SERVER_PORT}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"[*] Przyjęto połączenie od {client_address[0]}:{client_address[1]}")

            handle_client_connection(client_socket)
    except KeyboardInterrupt:
        print("[*] Zamykanie serwera.")
        server_socket.close()


if __name__ == "__main__":
    main()
