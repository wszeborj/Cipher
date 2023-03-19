# from memory_profiler import profile
AMOUNT_LETTERS = 26
AMOUNT_DIGITS = 10


def cipher(input_text: str, shift: int = 13):
    cipher_text = ''
    crypted = ''

    for i in input_text:
        if i.isupper():
            crypted = chr((ord(i) + shift - ord('A')) % AMOUNT_LETTERS + ord('A'))
        elif i.islower():
            crypted = chr((ord(i) + shift - ord('a')) % AMOUNT_LETTERS + ord('a'))
        elif i.isdigit():
            crypted = chr((ord(i) + shift - ord('0')) % AMOUNT_DIGITS + ord('0'))
        else:
            crypted = i
        cipher_text += crypted
    return cipher_text


def main():
    print(cipher('ZUPAzupa1', 47))


if __name__ == '__main__':
    main()
