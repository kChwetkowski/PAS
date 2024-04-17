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


    largest_msg_num = None
    largest_msg_size = 0
    for msg_info in msg_list:
        msg_num, msg_size = msg_info.decode().split()
        msg_size = int(msg_size)
        if msg_size > largest_msg_size:
            largest_msg_size = msg_size
            largest_msg_num = msg_num

    if largest_msg_num:
        response, msg_lines, _ = pop_conn.retr(largest_msg_num)
        msg_content = b"\n".join(msg_lines).decode("utf-8")
        print(f"Treść największej wiadomości (Wiadomość {largest_msg_num}): \n")
        print(msg_content)
    else:
        print("Brak wiadomości w skrzynce.")

except Exception as e:
    print(f"Wystąpił błąd: {e}")

finally:
    pop_conn.quit()
