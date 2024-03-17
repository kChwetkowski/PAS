import socket
def hex_to_dec(val):
    return int(val, 16)
def hex_to_ascii(val):
    return chr(val)
def process_ip_packet(packet):
    processed_packet = [hex_to_dec(x) for x in packet.split(' ')]
    X = processed_packet[9]
    Y = ".".join([str(x) for x in processed_packet[12:16]])
    Z = ".".join([str(x) for x in processed_packet[16:20]])
    W = packet.split(' ')[0][0]

    remaining_packet = packet[61:]
    print(f'Protokół: {X}')
    print(f'IP nadawcy: {Y}')
    print(f'IP odbiorcy: {Z}')
    print(f'Wersja protokołu: {W}')

    return W, X, Y, Z, remaining_packet


def process_tcp_packet(packet):
    processed_packet = [hex_to_dec(x) for x in packet.split(' ')]

    X = processed_packet[0] * 256 + processed_packet[1]
    Y = processed_packet[2] * 256 + processed_packet[3]
    Z = "".join([hex_to_ascii(x) for x in processed_packet[32:]])

    print(f'Port nadawcy: {X}')
    print(f'Port odbiorcy: {Y}')
    print(f'Wiadomość: {Z}')

    return X, Y, Z


def main():
    ip_packet = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"
    X, W, Y, Z, remaining_packet = process_ip_packet(ip_packet)
    server_address = ('127.0.0.1', 2911)
    message1 = f'zad15odpA;ver;{X};srcip;{Y};dstip;{Z};type;{W}'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(message1.encode(), server_address)
        data, server = sock.recvfrom(1024)
        response = data.decode()
        print('Odpowiedź serwera:', response)
    except ConnectionRefusedError:
        print('Błąd połączenia')
    finally:
        sock.close()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if response == 'TAK':
        Xb, Yb, Zb = process_tcp_packet(remaining_packet)
        message2 = f'zad15odpB;srcport;{Xb};dstport;{Yb};data;{Zb}'
        try:
            sock.sendto(message2.encode(), server_address)
            data, server = sock.recvfrom(1024)
            response = data.decode()
            print('Odpowiedź serwera:', response)
        except ConnectionRefusedError:
            print('Błąd połączenia')
        finally:
            sock.close()


if __name__ == "__main__":
    main()
