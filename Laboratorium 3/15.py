import socket

def extract_ip_fields(data):
    bytes_data = bytes.fromhex(data)
    version = bytes_data[0] >> 4
    src_ip = '.'.join(map(str, bytes_data[12:16]))  # Adres IP źródłowy
    dst_ip = '.'.join(map(str, bytes_data[16:20]))  # Adres IP docelowy
    protocol = bytes_data[9]

    return version, src_ip, dst_ip, protocol
def extract_tcp_fields(data):
    bytes_data = bytes.fromhex(data)
    src_port = int.from_bytes(bytes_data[20:22], byteorder='big')
    dst_port = int.from_bytes(bytes_data[22:24], byteorder='big')
    data_length = len(bytes_data) - 40
    return src_port, dst_port, data_length
def extract_udp_fields(data):
    bytes_data = bytes.fromhex(data)
    src_port = int.from_bytes(bytes_data[20:22], byteorder='big')
    dst_port = int.from_bytes(bytes_data[22:24], byteorder='big')
    data_length = len(bytes_data) - 28
    return src_port, dst_port, data_length

def main():
    ip_packet_hex = "4500004ef7fa400038069d33d4b6181b" \
                    "c0a800020b54b9a6fbf93c57c10a06c1" \
                    "801800e3ce9c00000101080a03a6eb01" \
                    "000bf8e56e6574776f726b2070726f67" \
                    "72616d6d696e672069732066756e"

    version, src_ip, dst_ip, protocol = extract_ip_fields(ip_packet_hex)
    message_A = f"zad15odpA;ver;{version};srcip;{src_ip};dstip;{dst_ip};type;{protocol}"

    server_address = "127.0.0.1"
    server_port = 2912

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(message_A.encode(), (server_address, server_port))
            response_A, _ = s.recvfrom(1024)
            if response_A.decode() == "TAK":
                if protocol == 6:
                    src_port, dst_port, data_length = extract_tcp_fields(ip_packet_hex)
                elif protocol == 17:
                    src_port, dst_port, data_length = extract_udp_fields(ip_packet_hex)
                else:
                    print("Unsupported protocol type")
                    return

                message_B = f"zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data_length}"
                s.sendto(message_B.encode(), (server_address, server_port))
                response_B, _ = s.recvfrom(1024)
                print(response_B.decode())
            else:
                print("Server returned BAD SYNTAX for message A")

    except socket.error as e:
        print(f"Błąd podczas komunikacji z serwerem: {e}")

if __name__ == "__main__":
    main()
