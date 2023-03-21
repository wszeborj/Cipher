import sys
import cipher
from file_handling import FileHandler


class Menu:
    def show(self):
        print('1. Szyfruj plik metodą rot13')
        print('2. Odszyfruj plik metodą rot13')
        print('3. Szyfruj plik metodą rot47')
        print('4. Odszyfruj plik metodą rot47')
        print('5. Zakoncz')

    def get_choice(self):
        try:
            choice = int(input('Wybierz opcję: '))
            if choice < 1 or 5 < choice:
                raise ValueError
            return choice
        except ValueError:
            print('Błędna opcja! Podaj numer z zakresu 1 - 5.')
            self.get_choice()


class Manager:
    def __init__(self):
        self.menu = Menu()

    def start(self):
        self.show_menu()

    def show_menu(self):
        while True:
            self.menu.show()
            self.execute()

    def execute(self):
        # TODO DICT / STRUCTURAL PATTERN MATCHING
        choice = self.menu.get_choice()
        dct = {1: self.cipher_rot13,
               2: self.decipher_rot13,
               3: self.cipher_rot47,
               4: self.decipher_rot47,
               5: self.decipher_exit}

        dct.get(choice)()

    def cipher_rot13(self):
        org_data = FileHandler.open_file(loaded_file_path='test_cipher.txt')
        ciphered_data = cipher.cipher(input_text=org_data, shift=13)
        FileHandler.save_file(file_path_to_save='test_cipher.txt', data=ciphered_data)

    def decipher_rot13(self):
        pass

    def cipher_rot47(self):
        pass

    def decipher_rot47(self):
        pass

    def decipher_exit(self):
        print('Koniec')
        sys.exit()


# TODO PLIK MAIN.py
def main():
    m = Manager()
    m.start()


if __name__ == '__main__':
    main()
