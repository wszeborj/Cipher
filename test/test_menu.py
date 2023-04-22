import unittest
from unittest.mock import Mock, patch
from functionality.menu import Menu
import tempfile
import os


class TestMenu(unittest.TestCase):
    def test_show_print(self):
        options = [
            "Szyfruj input metodą rot13",
            "Odszyfruj input metodą rot13",
            "Szyfruj input metodą rot47",
            "Odszyfruj input metodą rot47",
            "Pokaz buffor",
            "Zapisz buffor do pliku json",
            "Załaduj plik json do buffora",
            "Wyczyść buffor",
            "Zakoncz",
        ]
        mock_call_list = []
        for i, option in enumerate(options, start=1):
            mock_call_list.append(unittest.mock.call(f"{i}. {option}"))

        with unittest.mock.patch("builtins.print") as mock_print:
            Menu.show()
            mock_print.assert_has_calls(mock_call_list)

    def test_provide_value_to_get_choice_return_int(self):
        max_range_choice = 9
        checked_input = ["z", "123", 123, 5]
        prompt1 = "Błędna wartość podaj liczbę."
        prompt2 = f"Błędna opcja! Podaj numer z zakresu 1 - {max_range_choice}."
        with unittest.mock.patch("builtins.input", side_effect=checked_input):
            with unittest.mock.patch("builtins.print") as mock_print:
                choice = Menu.get_choice(no_of_options=max_range_choice)
                mock_print.assert_has_calls(
                    [
                        unittest.mock.call(prompt1),
                        unittest.mock.call(prompt2),
                        unittest.mock.call(prompt2),
                    ]
                )
                self.assertEquals(choice, 5)

    def test_provide_path_to_ask_path_loaded_file_return_path(self):
        expected = "test.json"
        prompt = "Nie ma takiego pliku. Spróbuj jeszcze raz."
        checked_input = [
            "zupa.txt",
            r"C:\Users\user\OneDrive\Dokumenty\cipher\test\test.txt",
            123,
            r"test.json",
        ]
        with open("./test.json", "w") as test_file:
            test_file.write("test data")

        with unittest.mock.patch("builtins.input", side_effect=checked_input):
            with unittest.mock.patch("builtins.print") as mock_print:
                path_loaded_file = Menu.ask_path_loaded_file()
                mock_print.assert_has_calls(
                    [unittest.mock.call(prompt) for _ in range(len(checked_input) - 1)]
                )
                self.assertEquals(path_loaded_file, expected)
        os.remove("test.json")

    def test_provide_path_which_exist_and_append_operation_to_ask_path_saved_file_return_existing_path(
        self,
    ):
        expected = ("test.json", "a")
        checked_input = ["test.json", "d"]
        with open("./test.json", "w") as test_file:
            test_file.write("test data")

        with unittest.mock.patch("builtins.input", side_effect=checked_input):
            path_saved_file = Menu.ask_path_saved_file()
        self.assertEquals(path_saved_file, expected)

        os.remove("test.json")

    def test_provide_path_which_exist_and_write_operation_to_ask_path_saved_file_return_existing_path(
        self,
    ):
        expected = ("test.json", "w")
        checked_input = ["test.json", "n"]
        with open("./test.json", "w") as test_file:
            test_file.write("test data")

        with unittest.mock.patch("builtins.input", side_effect=checked_input):
            path_saved_file = Menu.ask_path_saved_file()
        self.assertEquals(path_saved_file, expected)

        os.remove("test.json")

    def test_provide_path_which_doesnot_exist_and_write_operation_to_ask_path_saved_file_return_existing_path(
        self,
    ):
        expected = ("test.json", "w")
        checked_input = ["test.json"]

        with unittest.mock.patch("builtins.input", side_effect=checked_input):
            path_saved_file = Menu.ask_path_saved_file()
        self.assertEquals(path_saved_file, expected)

    def test_provide_letters_numbers_signs_to_ask_for_input_return_string(self):
        checked_input = ["", "zupa1.", "Ala ma kota"]
        with unittest.mock.patch("builtins.input", side_effect=checked_input):
            for i in checked_input:
                self.assertEquals(Menu.ask_for_input(), i)
