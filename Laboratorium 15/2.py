import socket
import requests
import select


def get_weather():
    api_key = 'd4af3e33095b8c43f1a6815954face64'
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Lublin&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15
        return f"Pogoda w Lublinie: {weather_description}. Temperatura: {temperature:.2f}°C"
    else:
        return "Błąd podczas pobierania danych pogodowych."


def main():
    server_address = ('127.0.0.1', 12345)
    buffer_size = 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Serwer pogody jest gotowy do nasłuchiwania...")

    inputs = [server_socket]
    outputs = []
    message_queues = {}

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

