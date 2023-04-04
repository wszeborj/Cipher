import os
import sys
import cipher
import json
from file_handling import FileHandler
from dataclasses import asdict
from cipher import CaesarCipher
from buffer import Buffer
from menu import Menu


class Manager:
    def __init__(self):
        self.menu = Menu()
        self.buffer = Buffer()

    def start(self) -> None:
        """
        Main
        """
        while True:
            self.menu.show()
            self.execute()

    def execute(self) -> None:
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
            5: self.buffer.show_all,
            6: self.save_text,
            7: self.exit
        }
        choice = self.menu.get_choice(no_of_options=len(dct.keys()))

        dct.get(choice)()

    def cipher_text_rot13(self):
        self.cipher_text(rot_shift=13, crypting=True)

    def decipher_text_rot13(self):
        self.cipher_text(rot_shift=13, crypting=False)

    def cipher_text_rot47(self):
        self.cipher_text(rot_shift=47, crypting=True)

    def decipher_text_rot47(self):
        self.cipher_text(rot_shift=47, crypting=False)

    # def show_buffer(self):
    #     self.buffer.show_all()

    def save_text(self):
        path_saved_file, operation = self.menu.ask_path_saved_file()
        input_str = ''
        for t in self.buffer.data:
            input_str += (str(t) + '\n')
        FileHandler.save_file(file_path_to_save=path_saved_file, data=input_str, operation=operation)

    def cipher_text(self, rot_shift: int, crypting: bool) -> None:
        """
        Method text from user to cipher, encrypt/decrypt it and add to buffer.
        """
        user_data = self.menu.ask_for_input()
        ciphered_data = CaesarCipher.encrypt_decrypt(input_text=user_data, shift=rot_shift, crypting=crypting)
        self.buffer.add(ciphered_data)

    # def cipher_rot(self, rot_shift: int, crypting: bool) -> None:
    #     if crypting:
    #         rot_status = 'crypted'
    #     else:
    #         rot_status = 'encrypted'
    #     path_loaded_file = self.menu.ask_path_loaded_file()
    #     org_data = FileHandler.open_file(loaded_file_path=path_loaded_file)
    #     ciphered_data = cipher.cipher(input_text=org_data, shift=rot_shift, crypting=crypting)
    #     data_to_save = {'text': ciphered_data, 'status': rot_status, 'rot_type': rot_shift}
    #     path_saved_file, operation = self.menu.ask_path_saved_file()
    #     FileHandler.save_file(file_path_to_save=path_saved_file, data=json.dumps(data_to_save), operation=operation)
    #
    # def cipher_rot13(self) -> None:
    #     self.cipher_rot(rot_shift=13, crypting=True)
    #
    # def decipher_rot13(self) -> None:
    #     self.cipher_rot(rot_shift=13, crypting=False)
    #
    # def cipher_rot47(self) -> None:
    #     self.cipher_rot(rot_shift=47, crypting=True)
    #
    # def decipher_rot47(self) -> None:
    #     self.cipher_rot(rot_shift=47, crypting=False)

    def exit(self) -> None:
        print('Koniec')
        sys.exit(0)

#
# # TODO PLIK MAIN.py
# def main():
#     m = Manager()
#     m.start()
#
#
# if __name__ == '__main__':
#     main()
