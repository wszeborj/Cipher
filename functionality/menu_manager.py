import os
import sys
import cipher
import json
from file_handling import FileHandler
from dataclasses import asdict
from cipher import Text


class Buffer:
    def __init__(self):
        self.__data = []

    @property
    def data(self):
        return self.__data

    def add(self, text: 'Text'):
        self.__data.append(text)

    def show_all(self):
        for t in self.__data:
            print(t)


class Menu:
    def show(self) -> None:
        print('1. Szyfruj input metodą rot13')
        print('2. Odszyfruj input metodą rot13')
        print('3. Szyfruj input metodą rot47')
        print('4. Odszyfruj input metodą rot47')
        print('5. Pokaz buffor')
        print('6. Zapisz buffor do pliku')
        print('7. Zakoncz')

    def get_choice(self) -> int:
        try:
            choice = int(input('Wybierz opcję: '))
            if choice < 1 or 7 < choice:
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

    def ask_for_input(self) -> str:
        user_input = input('Podaj treść: ')
        return user_input


class Manager:
    def __init__(self):
        self.menu = Menu()
        self.buffer = Buffer()

    def start(self) -> None:
        self.show_menu()

    def show_menu(self) -> None:
        while True:
            self.menu.show()
            self.execute()

    def execute(self) -> None:
        # TODO DICT / STRUCTURAL PATTERN MATCHING
        choice = self.menu.get_choice()
        dct = {
            # 1: self.cipher_rot13,
            # 2: self.decipher_rot13,
            # 3: self.cipher_rot47,
            # 4: self.decipher_rot47,
            # 5: self.decipher_exit
            1: self.cipher_text_rot13,
            2: self.decipher_text_rot13,
            3: self.cipher_text_rot47,
            4: self.decipher_text_rot47,
            5: self.show_buffer,
            6: self.save_text,
            7: self.decipher_exit
        }

        dct.get(choice)()

    def cipher_text_rot13(self):
        self.cipher_text(rot_shift=13, crypting=True)

    def decipher_text_rot13(self):
        self.cipher_text(rot_shift=13, crypting=False)

    def cipher_text_rot47(self):
        self.cipher_text(rot_shift=47, crypting=True)

    def decipher_text_rot47(self):
        self.cipher_text(rot_shift=47, crypting=False)

    def show_buffer(self):
        self.buffer.show_all()

    def save_text(self):
        path_saved_file, operation = self.menu.ask_path_saved_file()
        input_str = ''
        for t in self.buffer.data:
            input_str += str(t)
        FileHandler.save_file(file_path_to_save=path_saved_file, data=input_str, operation=operation)

    def cipher_text(self, rot_shift: int, crypting: bool) -> None:
        user_data = self.menu.ask_for_input()
        ciphered_data = cipher.cipher(input_text=user_data, shift=rot_shift, crypting=crypting)
        self.buffer.add(ciphered_data)

    def cipher_rot(self, rot_shift: int, crypting: bool) -> None:
        if crypting:
            rot_status = 'crypted'
        else:
            rot_status = 'encrypted'
        path_loaded_file = self.menu.ask_path_loaded_file()
        org_data = FileHandler.open_file(loaded_file_path=path_loaded_file)
        ciphered_data = cipher.cipher(input_text=org_data, shift=rot_shift, crypting=crypting)
        data_to_save = {'text': ciphered_data, 'status': rot_status, 'rot_type': rot_shift}
        path_saved_file, operation = self.menu.ask_path_saved_file()
        FileHandler.save_file(file_path_to_save=path_saved_file, data=json.dumps(data_to_save), operation=operation)

    def cipher_rot13(self) -> None:
        self.cipher_rot(rot_shift=13, crypting=True)

    def decipher_rot13(self) -> None:
        self.cipher_rot(rot_shift=13, crypting=False)

    def cipher_rot47(self) -> None:
        self.cipher_rot(rot_shift=47, crypting=True)

    def decipher_rot47(self) -> None:
        self.cipher_rot(rot_shift=47, crypting=False)

    def decipher_exit(self) -> None:
        print('Koniec')
        sys.exit()


# TODO PLIK MAIN.py
def main():
    m = Manager()
    m.start()


if __name__ == '__main__':
    main()
