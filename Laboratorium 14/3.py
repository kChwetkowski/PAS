import smtplib

def send_email():
    FROM_EMAIL = 'pas2017@interia.pl'
    PASSWORD = 'P4SInf2017'
    SMTP_SERVER = 'smtp.poczta.interia.pl'
    SMTP_PORT = 465

    to_email = input("Podaj adres odbiorcy: ")
    subject = input("Podaj temat wiadomości: ")
    body = input("Podaj treść wiadomości: ")

    message = f"From: {FROM_EMAIL}\r\nTo: {to_email}\r\nSubject: {subject}\r\n\r\n{body}\r\n"

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(FROM_EMAIL, PASSWORD)
            server.sendmail(FROM_EMAIL, to_email, message)
            print("Email wysłany pomyślnie.")
    except Exception as e:
        print(f"Błąd: {e}")

if __name__ == '__main__':
    send_email()
