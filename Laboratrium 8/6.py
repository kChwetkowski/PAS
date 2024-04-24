import socket

# Dane logowania
USER = "pasumcs@infumcs.edu"
PASSWORD = "P4SInf2017"

# Dane wiadomości
MESSAGES = {
    1: b"From: sender@example.com\r\nSubject: Test message 1\r\n\r\nThis is a test message 1.\r\n",
    2: b"From: sender@example.com\r\nSubject: Test message 2\r\n\r\nThis is a test message 2.\r\n",
    3: b"From: sender@example.com\r\nSubject: Test message 3\r\n\r\nThis is a test message 3.\r\n",
    4:b"From: sender@example.com\r\nSubject: Test message 3\r\n\r\nThis is a test message 3.\r\n",
}

def login(command):
    parts = command.split(b' ')
    if len(parts) == 3 and parts[0] == b'LOGIN' and parts[1] == USER.encode('utf-8') and parts[2] == PASSWORD.encode('utf-8'):
        return b'OK LOGIN completed.'
    else:
        return b'NO LOGIN failed.'

def select(command):
    parts = command.split(b' ')
    if len(parts) == 2 and parts[0] == b'SELECT' and parts[1] == b'INBOX':
        exists = len(MESSAGES)
        flags = b'\\Answered \\Flagged \\Deleted \\Seen \\Draft'
        permanent_flags = b'\\Answered \\Flagged \\Deleted \\Seen \\Draft \\*'
        uid_validity = b'1491554744'
        uid_next = b'3'
        highest_mod_seq = b'5'
        response = (
            b'* FLAGS (' + flags + b')\r\n' +
            b'* OK [PERMANENTFLAGS (' + permanent_flags + b')] Flags permitted.\r\n' +
            b'* ' + str(exists).encode() + b' EXISTS\r\n' +
            b'* 0 RECENT\r\n' +
            b'* OK [UIDVALIDITY ' + uid_validity + b'] UIDs valid\r\n' +
            b'* OK [UIDNEXT ' + uid_next + b'] Predicted next UID\r\n' +
            b'* OK [HIGHESTMODSEQ ' + highest_mod_seq + b'] Highest\r\n' +
            b'OK [READ-WRITE] SELECT completed.\r\n'
        )
        return response
    else:
        return b'NO SELECT failed.'


# Funkcja obsługująca pobieranie wiadomości
def fetch(command):
    try:
        message_num = int(command.split(b' ')[-1])
        if message_num in MESSAGES:
            return b'OK FETCH completed', MESSAGES[message_num]
        else:
            return b'NO FETCH failed', b''
    except ValueError:
        return b'NO FETCH failed', b''

# Funkcja obsługująca zmianę flag wiadomości
def store(command):
    try:
        parts = command.split(b' ')
        message_num = int(parts[0])
        if parts[1] == b'+FLAGS' and parts[2] == b'\\Seen':
            return b'OK STORE completed'
        elif parts[1] == b'+FLAGS' and parts[2] == b'\\Deleted':
            return b'OK STORE completed'
        else:
            return b'NO STORE failed'
    except (ValueError, IndexError):
        return b'NO STORE failed'

# Funkcja obsługująca usuwanie wiadomości
def expunge(command):
    if command == b'EXPUNGE':
        return b'OK EXPUNGE completed'
    else:
        return b'NO EXPUNGE failed'

# Funkcja obsługująca wylogowanie
def logout(command):
    if command == b'LOGOUT':
        return b'OK LOGOUT completed', True
    else:
        return b'NO LOGOUT failed', False

def handle_command(command):
    if command.startswith(b'LOGIN'):
        return login(command)
    elif command.startswith(b'SELECT'):
        return select(command)
    elif command.startswith(b'FETCH'):
        return fetch(command)
    elif command.startswith(b'STORE'):
        return store(command)
    elif command == b'EXPUNGE':
        return expunge(command)
    elif command == b'LOGOUT':
        return logout(command)
    else:
        return b'NO Unknown command.'

HOST = '127.0.0.1'
PORT = 1430

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Serwer IMAP nasłuchuje na {HOST}:{PORT}")

    connection, address = server_socket.accept()

    print(f"Połączono z klientem {address}")

    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            command = data.strip()
            response = handle_command(command)
            connection.sendall(response + b'\r\n')
            if command == b'LOGOUT':
                response, should_logout = logout(command)
                connection.sendall(response + b'\r\n')
                if should_logout:
                    break

    print(f"Rozłączono z klientem {address}")
