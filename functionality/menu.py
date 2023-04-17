import os


class Menu:
    def show(self) -> None:
        options = [
            "Szyfruj input metodą rot13",
            "Odszyfruj input metodą rot13",
            "Szyfruj input metodą rot47",
            "Odszyfruj input metodą rot47",
            "Pokaz buffor",
            "Zapisz buffor do pliku json",
            "Załaduj plik json do buffora",
            "Wyczyść buffor",
            "Zakoncz",
        ]
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    def get_choice(self, no_of_options: int) -> int:
        while True:
            try:
                choice = int(input("Wybierz opcję: "))
                if choice not in range(1, no_of_options + 1):
                    print(f"Błędna opcja! Podaj numer z zakresu 1 - {no_of_options}.")
                    continue
                return choice
            except ValueError:
                print(f"Błędna wartość podaj liczbę.")

    def ask_path_loaded_file(self) -> str:
        while True:
            path_loaded_file = input("Podaj scieżkę do otwieranego pliku: ")
            if os.path.exists(path_loaded_file):
                return path_loaded_file
            print("Nie ma takiego pliku. Spróbuj jeszcze raz.")

    def ask_path_saved_file(self) -> (str, str):
        while True:
            path_saved_file = input("Podaj scieżkę do zapisania pliku: ")
            operation = "w"
            if os.path.exists(path_saved_file):
                user_operation = input(
                    "Dodac do pliku (d) czu nadpisac plik (n)? (d/n): "
                )
                if user_operation.lower() == "d":
                    operation = "a"
                elif user_operation.lower() == "n":
                    operation = "w"
                else:
                    continue
            return path_saved_file, operation

    def ask_for_input(self) -> str:
        user_input = input("Podaj treść: ")
        return user_input
