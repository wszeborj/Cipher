from functionality.cipher import cipher
import pytest


def test_return_ciphered_rot13_string_after_providing_string_with_lower_upper_letters_number_signs():
    assert cipher(input_text='zupa1, ZUPA1.!?', shift=13, crypting=True) == 'mhcn4, MHCN4.!?'


def test_return_unciphered_rot13_string_after_providing_string_with_lower_upper_letters_number_signs():
    assert cipher(input_text='mhcn4, MHCN4.!?', shift=13, crypting=False) == 'zupa1, ZUPA1.!?'


def test_return_ciphered_rot47_string_after_providing_string_with_lower_upper_letters_number_signs():
    assert cipher(input_text='zupa1, ZUPA1.!?', shift=47, crypting=True) == 'upkv8, UPKV8.!?'


def test_return_unciphered_rot47_string_after_providing_string_with_lower_upper_letters_number_signs():
    assert cipher(input_text='upkv8, UPKV8.!?', shift=47, crypting=False) == 'zupa1, ZUPA1.!?'
