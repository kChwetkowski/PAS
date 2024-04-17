import poplib

POP3_SERVER = "dsmka.wintertoad.xyz"
POP3_PORT = 110
USERNAME = "test1@wintertoad.xyz"
PASSWORD = "P@ssw0rd"

try:
    pop_conn = poplib.POP3(POP3_SERVER, POP3_PORT)
    pop_conn.user(USERNAME)
    pop_conn.pass_(PASSWORD)
    num_messages = len(pop_conn.list()[1])

    print(f"Liczba wiadomości w skrzynce: {num_messages}")

except Exception as e:
    print(f"Wystąpił błąd: {e}")

finally:
    pop_conn.quit()
