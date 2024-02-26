def copy_file_content(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()

            with open(destination_file, 'w') as destination:
                destination.write(content)

        print(f"Plik został skopiowany do pomyślnie.")
    except FileNotFoundError:
        print("Podany plik nie istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

def main():
    source_file = input("Podaj nazwę pliku tekstowego: ")
    destination_file = "lab1zad1.txt"
    copy_file_content(source_file, destination_file)


if __name__ == "__main__":
    main()
