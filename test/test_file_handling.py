import tempfile
import unittest
from unittest.mock import patch
from functionality.file_handling import FileHandler

"""

    @staticmethod
    def save_file(file_path_to_save: str, data: str, operation: str = 'w') -> None:
        try:
            with open(file_path_to_save, operation) as file:
                file.write(data)
                file.write('\n')
        except OSError as err:
            print(f'{err=}, {type(err)=}')

"""


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_handler = FileHandler()

    def test_open_file(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            file_path = temp_file.name
            test_data = 'This is a test'

            FileHandler.save_file(file_path, test_data, 'w')

            with open(file_path, 'r') as file:
                contents = file.read()
                assert contents == test_data + "\n"

        # with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        #     temp_file.write('test')
        #     # temp_file.flush()
        #     # self.assertEqual(self.file_handler.open_file(temp_file.name), 'test')
        #
        # with open(temp_file.name, 'r') as temp_file_read:
        #     contents = temp_file_read.read()
        #     print(contents


if __name__ == '__main__':
    unittest.main()
