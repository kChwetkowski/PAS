import socket
def send_websocket_message(sock, message):
    frame = encode_websocket_frame(message)
    sock.sendall(frame)

def encode_websocket_frame(message):
    data_length = len(message)
    if data_length <= 125:
        frame = bytearray([0x81, data_length])
    elif data_length <= 65535:
        frame = bytearray([0x81, 126])
        frame.extend(data_length.to_bytes(2, byteorder='big'))
    else:
        frame = bytearray([0x81, 127])
        frame.extend(data_length.to_bytes(8, byteorder='big'))

    frame.extend(message.encode())
    return frame

def main():
    server_address = "127.0.0.1"
    server_port = 9999

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_address, server_port))

    message = "Hello, WebSocket Server!"
    send_websocket_message(sock, message)

    sock.close()

if __name__ == "__main__":
    main()
