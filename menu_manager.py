class Menu:
    def show(self):
        print('1. Szyfruj plik metodą rot13')
        print('2. Odszyfruj plik metodą rot13')
        print('3. Szyfruj plik metodą rot47')
        print('4. Odszyfruj plik metodą rot47')
        print('5. Zakoncz')

    def get_choice(self):
        try:
            return int(input('Wybierz opcję: '))
        except ValueError:
            print('Błędna opcja! Podaj numer z zakresu 1 - 5.')




