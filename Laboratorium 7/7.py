import poplib

POP3_SERVER = "dsmka.wintertoad.xyz"
POP3_PORT = 110
USERNAME = "test1@wintertoad.xyz"
PASSWORD = "P@ssw0rd"


try:
    pop_conn = poplib.POP3(POP3_SERVER, POP3_PORT)
    pop_conn.user(USERNAME)
    pop_conn.pass_(PASSWORD)
    response, msg_list, _ = pop_conn.list()
    total_bytes = sum(int(size.split()[1]) for size in msg_list)

    print(f"Liczba bajtów: {total_bytes} B")

except Exception as e:
    print(f"Wystąpił błąd: {e}")

finally:
    pop_conn.quit()
