# from memory_profiler import profile
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from buffer import Text


# class ROT(ABC):
#     def __init__(self):
#         pass
#
#     @abstractmethod
#     def encrypt(self):
#         pass
#
#     @abstractmethod
#     def decrypt(self):
#         pass
#
#     @staticmethod
#     def get_rot(rot_type: str):  # rot13, rot47
#         if rot_type == 'rot13':
#             return ROT13()
#         elif rot_type == 'rot47':
#             return ROT47()
#         else:
#             raise ValueError('Invalid ROT type')
#
#
# class ROT13(ROT):
#     def __init__(self):
#         super().__init__()
#
#     def encrypt(self):
#         pass
#
#     def decrypt(self):
#         pass
#
#
# class ROT47(ROT):
#     def __init__(self):
#         super().__init__()
#
#     def encrypt(self):
#         pass
#
#     def decrypt(self):
#         pass


class CaesarCipher:
    @staticmethod
    def shift_char(char: str, shift: int, first_ascii_char: str, is_encrypt: bool):
        amount_letters = 26
        amount_digits = 10
        if char.isdigit():
            amount_chars = amount_digits
        else:
            amount_chars = amount_letters

        if is_encrypt:
            return chr((ord(char) + shift - ord(first_ascii_char)) % amount_chars + ord(first_ascii_char))
        else:
            return chr((ord(char) - shift - ord(first_ascii_char)) % amount_chars + ord(first_ascii_char))

    @staticmethod
    def encrypt_decrypt(input_text: str, shift: int, crypting: bool = True) -> Text:
        cipher_text = ''

        for char in input_text:
            # if char.isupper():
            #     first_ascii_char = 'A'
            # elif char.islower():
            #     first_ascii_char = 'a'
            if char.isalpha():
                first_ascii_char = 'A' if char.isupper() else 'a'
            elif char.isdigit():
                first_ascii_char = '0'
            else:
                cipher_text += char
                continue
            crypted = CaesarCipher.shift_char(char=char, shift=shift, first_ascii_char=first_ascii_char,
                                              is_encrypt=crypting)
            cipher_text += crypted

        return Text(cipher_text, crypting, shift)

#
# def main():
#     print(cipher('ZUPAzupa1', 13))
#
#
# if __name__ == '__main__':
#     main()
