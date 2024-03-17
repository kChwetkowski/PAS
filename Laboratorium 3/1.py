import socket
import struct
import time

def get_ntp_time(host="ntp.task.gda.pl", port=123):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = bytearray(48)
    data[0] = 0x1B  # Kod pakietu zapytania NTP

    try:
        client.sendto(data, (host, port))
        data, _ = client.recvfrom(48)
        ntp_time = struct.unpack("!12I", data)[10] - 2208988800
        return time.ctime(ntp_time)
    except socket.timeout:
        print("Timeout - nie udało się pobrać danych z serwera NTP.")
    finally:
        client.close()

if __name__ == "__main__":
    ntp_time = get_ntp_time()
    if ntp_time:
        print("Aktualna data i czas pobrane z serwera NTP:", ntp_time)
