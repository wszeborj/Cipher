import unittest
from unittest.mock import Mock, patch
from functionality.menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()

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
            self.menu.show()
            mock_print.assert_has_calls(mock_call_list)

    def test_provide_value_to_get_choice_return_int(self):
        max_range_choice = 9
        checked_input = ["z", "123", 123, 5]
        prompt1 = "Błędna wartość podaj liczbę."
        prompt2 = f"Błędna opcja! Podaj numer z zakresu 1 - {max_range_choice}."
        with unittest.mock.patch("builtins.input", side_effect=checked_input):
            with unittest.mock.patch("builtins.print") as mock_print:
                choice = self.menu.get_choice(no_of_options=max_range_choice)
                mock_print.assert_has_calls(
                    [
                        unittest.mock.call(prompt1),
                        unittest.mock.call(prompt2),
                        unittest.mock.call(prompt2),
                    ]
                )
                self.assertEquals(choice, 5)

    def test_provide_path_to_ask_path_loaded_file_return_existing_path(self):
        pass

    def test_provide_path_and_operation_to_ask_path_saved_file_return_path_and_operation(
        self,
    ):
        pass

    def test_provide_letters_numbers_signs_to_ask_for_input_return_string(self):
        checked_input = ["", "zupa1.", "Ala ma kota"]
        with unittest.mock.patch("builtins.input", side_effect=checked_input):
            for i in checked_input:
                self.assertEquals(self.menu.ask_for_input(), i)
