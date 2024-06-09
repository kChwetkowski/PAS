import socket
import ssl


def send_email():
    HOST = 'interia.pl'
    PORT = 465
    FROM_EMAIL = 'pas2017@interia.pl'
    PASSWORD = 'P4SInf2017'
    CA_CERT = './GeoTrustGlobalCA.pem'

    to_email = input("Podaj adres odbiorcy: ")
    subject = input("Podaj temat wiadomości: ")
    body = input("Podaj treść wiadomości: ")

    message = f"From: {FROM_EMAIL}\r\nTo: {to_email}\r\nSubject: {subject}\r\n\r\n{body}\r\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations(CA_CERT)

    secure_sock = context.wrap_socket(sock, server_hostname=HOST)

    secure_sock.sendall(b'EHLO example.com\r\n')
    secure_sock.sendall(b'AUTH LOGIN\r\n')
    secure_sock.sendall(FROM_EMAIL.encode() + b'\r\n')
    secure_sock.sendall(PASSWORD.encode() + b'\r\n')
    secure_sock.sendall(b'MAIL FROM:<%s>\r\n' % FROM_EMAIL.encode())
    secure_sock.sendall(b'RCPT TO:<%s>\r\n' % to_email.encode())
    secure_sock.sendall(b'DATA\r\n')
    secure_sock.sendall(message.encode() + b'\r\n.\r\n')
    secure_sock.sendall(b'QUIT\r\n')

    secure_sock.close()
    sock.close()


if __name__ == '__main__':
    send_email()
