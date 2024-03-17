import socket
def hex_to_dec(val):
    return int(val, 16)
def hex_to_ascii(val):
    return chr(val)

def process_packet(packet):
    processed_packet = [hex_to_dec(x) for x in packet.split(' ')]
    X = processed_packet[0] * 256 + processed_packet[1]
    Y = processed_packet[2] * 256 + processed_packet[3]
    Z = "".join([hex_to_ascii(x) for x in processed_packet[32:]])
    print(f'Port nadawcy: {X}')
    print(f'Port odbiorcy: {Y}')
    print(f'Dane: {Z}')

    return X, Y, Z

def main():
    tcp_segment = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
    x, y, z = process_packet(tcp_segment)
    server_address = ('127.0.0.1', 2910)
    message = f'zad14odp;src;{x};dst;{y};data;{z}'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(message.encode(), server_address)
        data, server = sock.recvfrom(1024)
        response = data.decode()
        print('Odpowiedź serwera:', response)
    except ConnectionRefusedError:
        print('Błąd połączenia')
    finally:
        sock.close()

if __name__ == "__main__":
    main()
