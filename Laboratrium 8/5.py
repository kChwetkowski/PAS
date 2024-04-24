import imaplib


IMAP_SERVER = 'dsmka.wintertoad.xyz'
IMAP_PORT = 143
EMAIL = 'test1@wintertoad.xyz'
PASSWORD = 'P@ssw0rd'


def display_inbox_messages():
    status, messages = imap_conn.select('Inbox')

    if status == 'OK':
        status, message_numbers = imap_conn.search(None, 'ALL')

        if status == 'OK':
            for num in message_numbers[0].split():
                status, message_data = imap_conn.fetch(num, '(BODY.PEEK[HEADER.FIELDS (SUBJECT FROM)])')
                if status == 'OK' and message_data[0]:
                    msg_str = message_data[0][1].decode('utf-8')
                    subject = None
                    sender = None
                    for line in msg_str.split('\r\n'):
                        if line.startswith('Subject:'):
                            subject = line.split('Subject: ')[1]
                        elif line.startswith('From:'):
                            sender = line.split('From: ')[1]
                    if subject and sender:
                        print(f'{num}: {sender} - {subject}')
                    elif subject:
                        print(f'{num}: (Nieznany nadawca) - {subject}')
                    elif sender:
                        print(f'{num}: {sender} - (Brak tematu)')
                    else:
                        print(f'{num}: (Nieznany nadawca) - (Brak tematu)')

        else:
            print('Nie udało się pobrać listy wiadomości.')

    else:
        print('Nie udało się wybrać skrzynki "Inbox".')


imap_conn = imaplib.IMAP4(IMAP_SERVER, IMAP_PORT)
imap_conn.login(EMAIL, PASSWORD)

display_inbox_messages()
message_num = input('Podaj numer wiadomości do usunięcia: ')
status, response = imap_conn.fetch(message_num, '(UID)')
if status == 'OK' and response[0]:
    message_uid = response[0].split()[-1].decode('utf-8')
    status, response = imap_conn.store(message_num, '+FLAGS', '\\Deleted')
    if status == 'OK':
        status, response = imap_conn.expunge()
        if status == 'OK':
            print(f'Wiadomość o numerze {message_num} została usunięta.')
        else:
            print('Nie udało się usunąć wiadomości.')
    else:
        print('Nie udało się oznaczyć wiadomości do usunięcia.')
else:
    print('Nie udało się pobrać UID wybranej wiadomości.')

imap_conn.logout()