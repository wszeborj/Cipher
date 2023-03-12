import sys

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
        except ValueError:
            print('Błędna opcja! Podaj numer z zakresu 1 - 5.')
            self.get_choice()


class Manager:
    def __init__(self):
        self.menu = Menu()

    def start(self):
        self.menu.show()
        self.execute()

    def execute(self):
        choice = self.menu.get_choice()

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            sys.exit()


def main():
    m = Manager()
    m.start()


if __name__ == '__main__':
    main()