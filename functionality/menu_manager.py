import os
import sys
import cipher
import json
from file_handling import FileHandler


class Menu:
    def show(self) -> None:
        print('1. Szyfruj plik metodą rot13')
        print('2. Odszyfruj plik metodą rot13')
        print('3. Szyfruj plik metodą rot47')
        print('4. Odszyfruj plik metodą rot47')
        print('5. Zakoncz')

    def get_choice(self) -> int:
        try:
            choice = int(input('Wybierz opcję: '))
            if choice < 1 or 5 < choice:
                raise ValueError
            return choice
        except ValueError:
            print('Błędna opcja! Podaj numer z zakresu 1 - 5.')
            self.get_choice()

    def ask_path_loaded_file(self) -> str:
        while True:
            path_loaded_file = input('Podaj scieżkę do otwieranego pliku: ')
            if os.path.exists(path_loaded_file):
                return path_loaded_file
            print('Nie ma takiego pliku. Spróbuj jeszcze raz.')

    def ask_path_saved_file(self) -> (str, str):
        while True:
            path_loaded_file = input('Podaj scieżkę do zapisania pliku: ')
            operation = 'w'
            if os.path.exists(path_loaded_file):
                user_operation = input('Dodac do pliku (d) czu napisac plik (n)? (d/n): ')
                if user_operation.lower() == 'd':
                    operation = 'a'
                elif user_operation.lower() == 'n':
                    operation = 'w'
                else:
                    continue
            return path_loaded_file, operation


class Manager:
    def __init__(self):
        self.menu = Menu()

    def start(self) -> None:
        self.show_menu()

    def show_menu(self) -> None:
        while True:
            self.menu.show()
            self.execute()

    def execute(self) -> None:
        # TODO DICT / STRUCTURAL PATTERN MATCHING
        choice = self.menu.get_choice()
        dct = {1: self.cipher_rot13,
               2: self.decipher_rot13,
               3: self.cipher_rot47,
               4: self.decipher_rot47,
               5: self.decipher_exit}

        dct.get(choice)()

    def cipher_rot(self, rot_status: str, rot_shift: int) -> None:
        path_loaded_file = self.menu.ask_path_loaded_file()
        org_data = FileHandler.open_file(loaded_file_path=path_loaded_file)
        ciphered_data = cipher.cipher(input_text=org_data, shift=rot_shift)
        data_to_save = {'text': ciphered_data, 'status': rot_status, 'rot_type': rot_shift}
        path_saved_file, operation = self.menu.ask_path_saved_file()
        FileHandler.save_file(file_path_to_save=path_saved_file, data=json.dumps(data_to_save), operation=operation)

    def cipher_rot13(self) -> None:
        self.cipher_rot(rot_status='crypted', rot_shift=13)

    def decipher_rot13(self) -> None:
        self.cipher_rot(rot_status='encrypted', rot_shift=13)

    def cipher_rot47(self) -> None:
        self.cipher_rot(rot_status='crypted', rot_shift=47)

    def decipher_rot47(self) -> None:
        self.cipher_rot(rot_status='encrypted', rot_shift=47)

    def decipher_exit(self) -> None:
        print('Koniec')
        sys.exit()


# TODO PLIK MAIN.py
def main():
    m = Manager()
    m.start()


if __name__ == '__main__':
    main()
