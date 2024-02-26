def copy_file_content(source_file, destination_file):
    try:
        with open(source_file, 'rb') as source:
            content = source.read()

            with open(destination_file, 'wb') as destination:
                destination.write(content)

        print(f"Plik został skopiowany pomyślnie.")
    except FileNotFoundError:
        print("Podany plik nie istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

def main():
    source_file = input("Podaj nazwę pliku graficznego: ")
    destination_file = "lab1zad1.png"
    copy_file_content(source_file, destination_file)


if __name__ == "__main__":
    main()
