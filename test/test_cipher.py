from functionality.buffer import Text, Buffer
from functionality.cipher import CaesarCipher

import pytest


def test_return_ciphered_rot13_string_after_providing_string_with_lower_upper_letters_number_signs():
    assert CaesarCipher.encrypt_decrypt(input_text='zupa1, ZUPA1.!?', shift=13, crypting=True) == \
           Text(text='mhcn4, MHCN4.!?', status='encrypted', rot_type=13)


def test_return_unciphered_rot13_string_after_providing_string_with_lower_upper_letters_number_signs():
    assert CaesarCipher.encrypt_decrypt(input_text='mhcn4, MHCN4.!?', shift=13, crypting=False) == \
           Text(text='zupa1, ZUPA1.!?', status='decrypted', rot_type=13)


def test_return_ciphered_rot47_string_after_providing_string_with_lower_upper_letters_number_signs():
    assert CaesarCipher.encrypt_decrypt(input_text='zupa1, ZUPA1.!?', shift=47, crypting=True) == \
           Text(text='upkv8, UPKV8.!?', status='encrypted', rot_type=47)


def test_return_unciphered_rot47_string_after_providing_string_with_lower_upper_letters_number_signs():
    assert CaesarCipher.encrypt_decrypt(input_text='upkv8, UPKV8.!?', shift=47, crypting=False) == \
           Text(text='zupa1, ZUPA1.!?', status='decrypted', rot_type=47)
