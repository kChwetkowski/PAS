import smtplib
import ssl

def send_email():
    FROM_EMAIL = 'pas2017@interia.pl'
    PASSWORD = 'P4SInf2017'
    SMTP_SERVER = 'smtp.poczta.interia.pl'
    SMTP_PORT = 465
    CA_CERT = './GeoTrustGlobalCA.pem'

    to_email = input("Podaj adres odbiorcy: ")
    subject = input("Podaj temat wiadomości: ")
    body = input("Podaj treść wiadomości: ")

    message = f"From: {FROM_EMAIL}\r\nTo: {to_email}\r\nSubject: {subject}\r\n\r\n{body}\r\n"

    context = ssl.create_default_context()
    context.load_verify_locations(CA_CERT)

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(FROM_EMAIL, PASSWORD)
            server.sendmail(FROM_EMAIL, to_email, message)
            print("Email wysłany pomyślnie.")
    except Exception as e:
        print(f"Błąd: {e}")

if __name__ == '__main__':
    send_email()
