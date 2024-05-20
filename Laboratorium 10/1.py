import socket
import base64
import hashlib

def handshake(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    key = base64.b64encode(hashlib.sha1(base64.b64encode(hashlib.sha1(socket.gethostname().encode()).digest())).digest())

    handshake_request = (
        "GET / HTTP/1.1\r\n"
        "Host: %s:%s\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "Sec-WebSocket-Key: %s\r\n"
        "Sec-WebSocket-Version: 13\r\n"
        "\r\n" % (host, port, key.decode('utf-8')))
    sock.send(handshake_request.encode())

    handshake_response = sock.recv(4096)

    if b"101 Switching Protocols" not in handshake_response:
        print("Nieudane nawiązanie połączenia")
        return None
    else:
        print("Nawiązano połączenie")

    return sock

def send_message(sock, message):
    opcode = 0x81
    payload = message.encode('utf-8')
    payload_length = len(payload)

    if payload_length <= 125:
        frame = bytearray([opcode, payload_length]) + payload
    elif payload_length <= 65535:
        frame = bytearray([opcode, 126]) + payload_length.to_bytes(2, byteorder='big') + payload
    else:
        frame = bytearray([opcode, 127]) + payload_length.to_bytes(8, byteorder='big') + payload

    sock.sendall(frame)

    response = sock.recv(4096)
    print("Otrzymano odpowiedź:", response)

host = "echo.websocket.events"
port = 80

sock = handshake(host, port)

if sock:
    message = "Hello, WebSocket!"
    send_message(sock, message)
    sock.close()
