import tempfile
import unittest
import json
import os
import pytest
from unittest.mock import patch
from functionality.file_handling import FileHandler


# def test_xyz():
# with pytest.raises(json.decoder.JSONDecodeError):


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_handler = FileHandler()
        self.file_path = r"C:\Users\user\OneDrive\Dokumenty\cipher\test\test.json"
        self.data1 = [{"text": "mhcn4", "status": "encrypted", "rot_type": 13}]
        self.data2 = [{"text": "mhcn5", "status": "encrypted", "rot_type": 13}]

    # def test_open_file(self):
    #     with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
    #         file_path = temp_file.name
    #         test_data = [{"text": "mhcn4", "status": "encrypted", "rot_type": 13}]
    #
    #         FileHandler.save_file(file_path, test_data, "w")
    #
    #         with open(file_path, "r") as file:
    #             contents = file.read()
    #             assert contents == test_data

    def test_provide_path_to_json_file_to_open_file_return_list_dictionaries(self):
        with open(self.file_path, "w") as json_file:
            json.dump(self.data1, json_file)

        loaded_data = FileHandler.open_file(self.file_path)
        self.assertEquals(loaded_data, self.data1)
        os.remove(self.file_path)

    def test_provide_path_to_invalid_json_file_to_open_file_return_error(self):
        with open(self.file_path, "w") as inv_json_file:
            inv_json_file.write("test data")

        with unittest.mock.patch("builtins.print") as mock_print:
            loaded_inv_data = FileHandler.open_file(self.file_path)
            mock_print.assert_called_with(
                f"Expecting value: line 1 column 1 (char 0), File is not json file"
            )
            self.assertEquals(loaded_inv_data, [])
        os.remove(self.file_path)

    def test_provide_data_for_save_file_and_write_file_with_saved_data(self):
        operation = "w"

        FileHandler.save_file(
            file_path_to_save=self.file_path, data=self.data1, operation=operation
        )
        with open(self.file_path, "r") as json_file:
            saved_data = json.load(json_file)
        self.assertEquals(saved_data, self.data1)
        os.remove(self.file_path)

    def test_provide_data_for_save_file_and_append_file_with_saved_data(self):
        operation = "a"
        expected_data = self.data2 + self.data1

        with open(self.file_path, "w") as json_file:
            json.dump(self.data1, json_file)

        FileHandler.save_file(
            file_path_to_save=self.file_path, data=self.data2, operation=operation
        )
        with open(self.file_path, "r") as json_file:
            saved_data = json.load(json_file)
        self.assertEquals(saved_data, expected_data)
        os.remove(self.file_path)
