import socket
def hex_to_dec(val):
    return int(val, 16)
def hex_to_ascii(val):
    return chr(val)

def process_packet(packet):
    processed_packet = [hex_to_dec(x) for x in packet.split(' ')]
    X = processed_packet[0] * 256 + processed_packet[1]
    Y = processed_packet[2] * 256 + processed_packet[3]
    Z = "".join([hex_to_ascii(x) for x in processed_packet[8:]])
    print(f'Port nadawcy: {X}')
    print(f'Port odbiorcy: {Y}')
    print(f'Dane: {Z}')

    return X, Y, Z

udp_datagram = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
x, y, z = process_packet(udp_datagram)
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
