import socket
import threading
import struct

def handle_client_connection(client_socket):
    try:
        request = client_socket.recv(1024)

        if b"Upgrade: websocket" in request:
            response = b"HTTP/1.1 101 Switching Protocols\r\n"
            response += b"Upgrade: websocket\r\n"
            response += b"Connection: Upgrade\r\n"
            response += b"Sec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk=\r\n\r\n"

            client_socket.sendall(response)

            while True:
                data = client_socket.recv(1024)
                if not data:
                    break

                message = decode_websocket_frame(data)
                print("[*] Received message:", message)
                send_websocket_message(client_socket, message)

    finally:
        client_socket.close()

def decode_websocket_frame(frame):
    payload_length = frame[1] & 127
    if payload_length == 126:
        mask_offset = 4
        payload_length = struct.unpack("!H", frame[2:4])[0]
    elif payload_length == 127:
        mask_offset = 10
        payload_length = struct.unpack("!Q", frame[2:10])[0]
    else:
        mask_offset = 2

    mask = frame[mask_offset:mask_offset + 4]
    encrypted_data = frame[mask_offset + 4:]

    data = bytearray()
    for i in range(len(encrypted_data)):
        data.append(encrypted_data[i] ^ mask[i % 4])

    return data.decode("utf-8", errors="ignore")

def encode_websocket_frame(message):
    data_length = len(message)
    if data_length <= 125:
        frame = bytearray([0x81, data_length])
    elif data_length <= 65535:
        frame = bytearray([0x81, 126])
        frame.extend(struct.pack("!H", data_length))
    else:
        frame = bytearray([0x81, 127])
        frame.extend(struct.pack("!Q", data_length))

    frame.extend(message.encode())
    return frame

def send_websocket_message(client_socket, message):
    frame = encode_websocket_frame(message)
    client_socket.sendall(frame)

def start_server():
    server_address = ("127.0.0.1", 9999)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("[*] Listening on {}:{}".format(server_address[0], server_address[1]))

    while True:
        client_socket, client_address = server_socket.accept()
        print("[*] Accepted connection from {}:{}".format(client_address[0], client_address[1]))

        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_handler.start()

start_server()
