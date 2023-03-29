# from memory_profiler import profile
AMOUNT_LETTERS = 26
AMOUNT_DIGITS = 10


def crypt_char(char: str, shift: int, first_ascii_char: str):
    if char.isdigit():
        return chr((ord(char) + shift - ord(first_ascii_char)) % AMOUNT_DIGITS + ord(first_ascii_char))
    return chr((ord(char) + shift - ord(first_ascii_char)) % AMOUNT_LETTERS + ord(first_ascii_char))


def encrypt_char(char: str, shift: int, first_ascii_char: str):
    if char.isdigit():
        return chr((ord(char) - shift - ord(first_ascii_char)) % AMOUNT_DIGITS + ord(first_ascii_char))
    return chr((ord(char) - shift - ord(first_ascii_char)) % AMOUNT_LETTERS + ord(first_ascii_char))


def cipher(input_text: str, shift: int, crypting: bool = True) -> str:
    cipher_text = ''
    if crypting:
        for char in input_text:
            if char.isupper():
                crypted = crypt_char(char=char, shift=shift, first_ascii_char='A')
            elif char.islower():
                crypted = crypt_char(char=char, shift=shift, first_ascii_char='a')
            elif char.isdigit():
                crypted = crypt_char(char=char, shift=shift, first_ascii_char='0')
            else:
                crypted = char
            cipher_text += crypted
    else:
        for char in input_text:
            if char.isupper():
                encrypted = encrypt_char(char=char, shift=shift, first_ascii_char='A')
            elif char.islower():
                encrypted = encrypt_char(char=char, shift=shift, first_ascii_char='a')
            elif char.isdigit():
                encrypted = encrypt_char(char=char, shift=shift, first_ascii_char='0')
            else:
                encrypted = char
            cipher_text += encrypted
    return cipher_text


def main():
    print(cipher('ZUPAzupa1', 13))


if __name__ == '__main__':
    main()
