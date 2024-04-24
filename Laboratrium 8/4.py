import imaplib
import email
from email.header import decode_header

IMAP_SERVER = 'dsmka.wintertoad.xyz'
IMAP_PORT = 143
EMAIL = 'test1@wintertoad.xyz'
PASSWORD = 'P@ssw0rd'

imap_conn = imaplib.IMAP4(IMAP_SERVER, IMAP_PORT)
imap_conn.login(EMAIL, PASSWORD)

status, messages = imap_conn.select('Inbox')

if status == 'OK':
    status, unseen_messages = imap_conn.search(None, 'UNSEEN')

    if status == 'OK':
        if unseen_messages[0]:
            message_numbers = unseen_messages[0].split()

            for num in message_numbers:
                status, data = imap_conn.fetch(num, '(RFC822)')
                if status == 'OK':
                    raw_email = data[0][1]
                    msg = email.message_from_bytes(raw_email)

                    print('-----------------------------')
                    print(f'Nieprzeczytana wiadomość:')
                    print('Od:', msg['From'])
                    print('Temat:', decode_header(msg['Subject'])[0][0])
                    print('Treść:')
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            print(part.get_payload(decode=True).decode('utf-8'))

                    imap_conn.store(num, '+FLAGS', '\\Seen')
                    print('Wiadomość oznaczona jako przeczytana.\n')

            print('Wszystkie nieprzeczytane wiadomości zostały wyświetlone.')

        else:
            print('Brak nieprzeczytanych wiadomości.')

    else:
        print('Nie udało się pobrać listy nieprzeczytanych wiadomości.')

else:
    print('Nie udało się wybrać skrzynki "Inbox".')

imap_conn.logout()
