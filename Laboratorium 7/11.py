import poplib
import email
import os

POP3_SERVER = "dsmka.wintertoad.xyz"
POP3_PORT = 110
USERNAME = "test1@wintertoad.xyz"
PASSWORD = "P@ssw0rd"


SAVE_PATH = "/home/student/Pulpit/Laboratorium 7/"

try:
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    pop_conn = poplib.POP3(POP3_SERVER, POP3_PORT)
    pop_conn.user(USERNAME)
    pop_conn.pass_(PASSWORD)
    response, msg_list, _ = pop_conn.list()

    for msg_info in msg_list:
        msg_num, _ = msg_info.decode().split()
        response, msg_lines, _ = pop_conn.retr(int(msg_num))
        msg_content = b"\n".join(msg_lines).decode("utf-8")
        msg = email.message_from_string(msg_content)

        if msg.get_content_maintype() == 'multipart':
            for part in msg.walk():
                if part.get_content_maintype() == 'image':
                    filename = part.get_filename()
                    attachment = part.get_payload(decode=True)

                    if filename:
                        filepath = os.path.join(SAVE_PATH, filename)
                        with open(filepath, 'wb') as f:
                            f.write(attachment)
                        print(f"Zapisano obrazek: {filepath}")

except Exception as e:
    print(f"Wystąpił błąd: {e}")

finally:
    # Zakończenie sesji POP3
    pop_conn.quit()
