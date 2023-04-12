import sys
import json
from file_handling import FileHandler
from cipher import CaesarCipher
from buffer import Buffer
from menu import Menu


class Manager:
    def __init__(self):
        self.menu = Menu()
        self.buffer = Buffer()

    def start(self) -> None:
        while True:
            self.menu.show()
            self.execute()

    def execute(self) -> None:
        # dct = {
        #     1: (self.cipher_text, 'Wybierz tekst')
        # }
        dct = {
            1: self.cipher_text_rot13,
            2: self.decipher_text_rot13,
            3: self.cipher_text_rot47,
            4: self.decipher_text_rot47,
            5: self.buffer.show_all,
            6: self.save_text,
            7: self.load_file,
            8: self.buffer.clear,
            9: self.exit,
        }
        choice = self.menu.get_choice(no_of_options=len(dct.keys()))

        dct.get(choice)()

    def cipher_text_rot13(self):
        self.perform_cipher(rot_shift=13, crypting=True)

    def decipher_text_rot13(self):
        self.perform_cipher(rot_shift=13, crypting=False)

    def cipher_text_rot47(self):
        self.perform_cipher(rot_shift=47, crypting=True)

    def decipher_text_rot47(self):
        self.perform_cipher(rot_shift=47, crypting=False)

    def save_text(self):
        path_saved_file, operation = self.menu.ask_path_saved_file()
        FileHandler.save_file(
            file_path_to_save=path_saved_file,
            data=self.buffer.data,
            operation=operation,
        )

    def load_file(self):
        loaded_file_path = self.menu.ask_path_loaded_file()
        loaded_data = FileHandler.open_file(loaded_file_path=loaded_file_path)
        self.buffer.extend(loaded_data)
        self.buffer.show_all()

    def perform_cipher(self, rot_shift: int, crypting: bool) -> None:
        """
        Method text from user to cipher, encrypt/decrypt it and add to buffer.
        """
        user_data = self.menu.ask_for_input()
        ciphered_data = CaesarCipher.encrypt_decrypt(
            input_text=user_data, shift=rot_shift, crypting=crypting
        )
        self.buffer.add(ciphered_data)

    def exit(self) -> None:
        print("Koniec")
        sys.exit(0)
