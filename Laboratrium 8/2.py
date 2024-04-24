import imaplib

IMAP_SERVER = 'dsmka.wintertoad.xyz'
IMAP_PORT = 143
EMAIL = 'test1@wintertoad.xyz'
PASSWORD = 'P@ssw0rd'

imap_conn = imaplib.IMAP4(IMAP_SERVER, IMAP_PORT)
imap_conn.login(EMAIL, PASSWORD)

status, messages = imap_conn.select('Inbox')

if status == 'OK':
    status, data = imap_conn.search(None, 'ALL')
    if status == 'OK':
        message_count = len(data[0].split())
        print(f'Liczba wiadomości w skrzynce "Inbox": {message_count}')
    else:
        print('Nie udało się pobrać informacji o liczbie wiadomości.')
else:
    print('Nie udało się wybrać skrzynki "Inbox".')

# Zamknięcie połączenia
imap_conn.logout()
