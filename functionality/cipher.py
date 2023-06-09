from functionality.buffer import Text


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
            return chr(
                (ord(char) + shift - ord(first_ascii_char)) % amount_chars
                + ord(first_ascii_char)
            )
        return chr(
            (ord(char) - shift - ord(first_ascii_char)) % amount_chars
            + ord(first_ascii_char)
        )

    @staticmethod
    def encrypt_decrypt(input_text: str, shift: int, crypting: bool = True) -> Text:
        cipher_text = ""

        for char in input_text:
            if char.isalpha():
                first_ascii_char = "A" if char.isupper() else "a"
            elif char.isdigit():
                first_ascii_char = "0"
            else:
                cipher_text += char
                continue
            crypted = CaesarCipher.shift_char(
                char=char,
                shift=shift,
                first_ascii_char=first_ascii_char,
                is_encrypt=crypting,
            )
            cipher_text += crypted
        print("Rezultat: ", cipher_text)
        return Text(text=cipher_text, rot_type=shift, status=crypting)
