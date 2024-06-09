import requests

def fetch_html():
    url = "https://127.0.0.1:4443"
    CA_CERT = './server.pem'

    try:
        response = requests.get(url, verify=CA_CERT)
        response.raise_for_status()
        with open("output.html", "wb") as f:
            f.write(response.content)
        print("HTML został zapisany do output.html")
    except requests.exceptions.RequestException as e:
        print(f"Błąd: {e}")

if __name__ == '__main__':
    fetch_html()
