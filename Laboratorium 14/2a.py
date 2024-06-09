import socket
import ssl


def fetch_html():
    HOST = 'httpbin.org'
    PORT = 443

    request = (
        "GET /html HTTP/1.1\r\n"
        "Host: httpbin.org\r\n"
        "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Safari/7.0.3\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    secure_sock = context.wrap_socket(sock, server_hostname=HOST)

    secure_sock.sendall(request.encode())
    response = secure_sock.recv(4096)

    with open("output.html", "wb") as f:
        f.write(response)

    secure_sock.close()
    sock.close()


if __name__ == '__main__':
    fetch_html()
