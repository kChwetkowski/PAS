import socket

def extract_udp_fields(data):
    bytes_data = bytes.fromhex(data)

    src_port = int.from_bytes(bytes_data[:2], byteorder='big')
    dst_port = int.from_bytes(bytes_data[2:4], byteorder='big')
    data_length = len(bytes_data) - 8

    return src_port, dst_port, data_length

def check_msg_syntax(txt):
    txt = txt.decode()
    s = txt.split(";")
    if len(s) != 7:
        return "BAD_SYNTAX"
    return "OK"
def main():
    udp_data_hex = \
        "ed740b550024effd70726f677261" \
        "6d6d696e6720696e20707974686f" \
        "6e2069732066756e"

    src_port, dst_port, data_length = extract_udp_fields(udp_data_hex)

    message = f"zad14odp;src;{src_port};dst;{dst_port};data;{data_length}"

    server_address = "127.0.0.1"
    server_port = 2910

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(message.encode(), (server_address, server_port))
            response, _ = s.recvfrom(1024)
            answer = check_msg_syntax(response)
            print(answer)
    except socket.error as e:
        print(f"Błąd podczas komunikacji z serwerem: {e}")

if __name__ == "__main__":
    main()
