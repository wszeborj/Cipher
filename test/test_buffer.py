from functionality.buffer import Buffer, Text
from functionality.cipher import CaesarCipher
import pytest


def test_add_obj_text_to_buffer_return_added_obj_buffer():
    buffer = Buffer.add(Text(text='Zupa1.', rot_type=13, status='encrypted'))
    assert buffer.data == [{"text": "mhcn4", "status": "encrypted", "rot_type": 13}]


def test_extend_list_of_dict_to_buffer_return_extended_list():
    pass


def test_clear_list_buffer_return_empty_list():
    pass
