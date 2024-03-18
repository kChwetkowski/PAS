import socket

def operations(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Can't divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"

def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 2010
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        print(f"Serwer nasłuchuje na {SERVER_HOST}:{SERVER_PORT}")

        while True:
            data, client_address = server_socket.recvfrom(1024)
            print(f"Odebrano wiadomość od klienta {client_address}: {data.decode()}")

            try:
                num1, op, num2 = data.decode().split()
                num1 = float(num1)
                num2 = float(num2)
                result = operations(num1, op, num2)
                server_socket.sendto(str(result).encode(), client_address)
                print(f"Wysłano wynik do klienta {client_address}: {result}")
            except ValueError:
                error_msg = "Error: invalid input format"
                server_socket.sendto(error_msg.encode(), client_address)
                print(f"Wysłano komunikat o błędzie do klienta {client_address}: {error_msg}")

    except socket.error as e:
        print(f"Błąd podczas działania serwera: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
