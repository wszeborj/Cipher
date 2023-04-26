import unittest
from dataclasses import asdict
from unittest.mock import Mock, patch

from functionality.buffer import Buffer, Text


class TestText(unittest.TestCase):
    def test_set_status_to_encrypted_when_true_status_was_provided(self):
        provided = Text(text="", rot_type=13, status=True)
        expected = Text(text="", rot_type=13, status="encrypted")
        assert provided == expected

    def test_set_status_to_decrypted_when_false_status_was_provided(self):
        provided = Text(text="", rot_type=13, status=False)
        expected = Text(text="", rot_type=13, status="decrypted")
        assert provided == expected

    def test_set_status_to_decrypted_when_string_status_was_provided(self):
        provided = Text(text="", rot_type=13, status="False")
        expected = Text(text="", rot_type=13, status="encrypted")
        assert provided == expected


class TestBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer = Buffer()
        self.text1 = Text(text="Ala ma kota", rot_type=13, status=False)
        self.text2 = Text(text="zupa1.", rot_type=47, status=True)
        self.dict1 = asdict(self.text1)
        self.dict2 = asdict(self.text2)

    def test_add_obj_text_to_buffer_return_list_of_dict(self):
        self.buffer.add(self.text1)
        assert self.buffer.data == [self.dict1]
        self.buffer.add(self.text2)
        assert self.buffer.data == [self.dict1, self.dict2]

    def test_extend_list_of_dict_to_buffer_return_extended_list(self):
        self.buffer.extend([self.dict1, self.dict2])
        assert self.buffer.data == [self.dict1, self.dict2]

    def test_clear_list_buffer_return_empty_list(self):
        self.buffer.extend([self.dict1, self.dict2])
        self.buffer.clear()
        assert self.buffer.data == []

    def test_show_all_buffer_data(self):
        self.buffer.add(self.text1)
        self.buffer.add(self.text2)
        with unittest.mock.patch("builtins.print") as mock_print:
            self.buffer.show_all()
            mock_print.assert_called_with([self.dict1, self.dict2])

    @patch("builtins.print")
    def test_show_all_buffer_data_2(self, mock_print):
        self.buffer.add(self.text1)
        self.buffer.add(self.text2)
        self.buffer.show_all()
        mock_print.assert_called_with([self.dict1, self.dict2])
