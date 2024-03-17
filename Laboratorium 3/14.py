import socket

def extract_tcp_fields(data):
    bytes_data = bytes.fromhex(data)
    src_port = int.from_bytes(bytes_data[:2], byteorder='big')
    dst_port = int.from_bytes(bytes_data[2:4], byteorder='big')
    data_length = len(bytes_data) - 20

    return src_port, dst_port, data_length
def main():
    tcp_segment_hex = "0b54898b1f9a18ecbbb164f28018" \
                      "00e36771000000101080a02c1a4ee" \
                      "001a4cee68656c6c6f203a29"

    src_port, dst_port, data_length = extract_tcp_fields(tcp_segment_hex[:28])
    message = f"zad13odp;src;{src_port};dst;{dst_port};data;{data_length}"

    server_address = "127.0.0.1"
    server_port = 2911

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(message.encode(), (server_address, server_port))
            response, _ = s.recvfrom(1024)

            print(response.decode())
    except socket.error as e:
        print(f"Błąd podczas komunikacji z serwerem: {e}")

if __name__ == "__main__":
    main()
