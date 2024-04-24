import imaplib
import re

IMAP_SERVER = 'dsmka.wintertoad.xyz'
IMAP_PORT = 143
EMAIL = 'test1@wintertoad.xyz'
PASSWORD = 'P@ssw0rd'

imap_conn = imaplib.IMAP4(IMAP_SERVER, IMAP_PORT)
imap_conn.login(EMAIL, PASSWORD)

status, folders = imap_conn.list()
total_messages = 0

if status == 'OK':
    for folder_info in folders:
        folder_info = folder_info.decode('utf-8')

        match = re.match(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)', folder_info)
        if match:
            folder_name = match.group('name')
            folder_name = folder_name.strip('"')
            imap_conn.select(folder_name)

            status, data = imap_conn.status(folder_name, "(MESSAGES)")

            if status == 'OK':
                messages_count = int(data[0].decode('utf-8').split()[2].strip(')'))
                print(f'Liczba wiadomości w skrzynce "{folder_name}": {messages_count}')
                total_messages += messages_count
            else:
                print(f'Nie udało się pobrać informacji o liczbie wiadomości w skrzynce "{folder_name}".')

    print(f'\nLiczba wiadomości we wszystkich skrzynkach łącznie: {total_messages}')

else:
    print('Nie udało się pobrać listy skrzynek.')

imap_conn.logout()