import os


class Menu:
    @staticmethod
    def show() -> None:
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

    @staticmethod
    def get_choice(no_of_options: int) -> int:
        while True:
            try:
                choice = int(input("Wybierz opcję: "))
                if choice not in range(1, no_of_options + 1):
                    print(f"Błędna opcja! Podaj numer z zakresu 1 - {no_of_options}.")
                    continue
                return choice
            except ValueError:
                print(f"Błędna wartość podaj liczbę.")

    @staticmethod
    def ask_path_loaded_file() -> str:
        while True:
            path_loaded_file = input("Podaj scieżkę do otwieranego pliku: ")
            if os.path.exists(path_loaded_file):
                return path_loaded_file
            print("Nie ma takiego pliku. Spróbuj jeszcze raz.")

    @staticmethod
    def ask_path_saved_file() -> (str, str):
        path_saved_file = self.ask_path_loaded_file()
        operation = "w"
        user_operation = input("Dodac do pliku (d) czu nadpisac plik (n)? (d/n): ")
        if user_operation.lower() == "d":
            operation = "a"
        elif user_operation.lower() == "n":
            operation = "w"
        return path_saved_file, operation

    @staticmethod
    def ask_for_input() -> str:
        user_input = input("Podaj treść: ")
        return user_input
