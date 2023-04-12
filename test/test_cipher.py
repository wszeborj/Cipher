from functionality.buffer import Text, Buffer
from functionality.cipher import CaesarCipher

import pytest


class TestCipher:
    def setup_method(self):
        self.word = "zupa1, ZUPA1.!?"
        self.word_13 = "mhcn4, MHCN4.!?"
        self.word_47 = "upkv8, UPKV8.!?"

    def test_return_encrypted_rot13_string_after_providing_string_with_lower_upper_letters_number_signs(
        self,
    ):
        assert CaesarCipher.encrypt_decrypt(
            input_text=self.word, shift=13, crypting=True
        ) == Text(text=self.word_13, status="encrypted", rot_type=13)

    def test_return_decrypted_rot13_string_after_providing_string_with_lower_upper_letters_number_signs(
        self,
    ):
        assert CaesarCipher.encrypt_decrypt(
            input_text=self.word_13, shift=13, crypting=False
        ) == Text(text=self.word, status="decrypted", rot_type=13)

    def test_return_encrypted_rot47_string_after_providing_string_with_lower_upper_letters_number_signs(
        self,
    ):
        assert CaesarCipher.encrypt_decrypt(
            input_text=self.word, shift=47, crypting=True
        ) == Text(text=self.word_47, status="encrypted", rot_type=47)

    def test_return_decrypted_rot47_string_after_providing_string_with_lower_upper_letters_number_signs(
        self,
    ):
        assert CaesarCipher.encrypt_decrypt(
            input_text=self.word_47, shift=47, crypting=False
        ) == Text(text=self.word, status="decrypted", rot_type=47)
