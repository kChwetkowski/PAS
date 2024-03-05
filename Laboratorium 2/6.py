import socket

def udp_client(host="127.0.0.1", port=2902):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (host, port)

        while True:
            num1 = input("Wpisz pierwszą liczbę: ")
            operator = input("Wpisz operator (+, -, *, /): ")
            num2 = input("Wpisz drugą liczbę: ")
            # message = f"{num1} {operator} {num2}"
            client_socket.sendto(num1.encode(), server_address)
            client_socket.sendto(operator.encode(), server_address)
            client_socket.sendto(num2.encode(), server_address)
            response, _ = client_socket.recvfrom(1024)
            print("Otrzymana odpowiedź od serwera:", response.decode())
            if num1.lower() == "stop":
                break

    except socket.error as e:
        print("Wystąpił błąd podczas połączenia:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    udp_client()
