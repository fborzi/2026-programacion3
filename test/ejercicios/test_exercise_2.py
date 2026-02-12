import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from test.utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_INT_WITHOUT_COLON


class TestExercise2(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio2"

    def run_exercise(self, *inputs: int) -> list[str]:
        """Runs the exercise with the given inputs and captures the output."""
        with patch("builtins.input", side_effect=list(inputs)):
            with patch("sys.stdout", new = io.StringIO()) as fake_out:
                if self.MODULE_NAME in sys.modules:
                    importlib.reload(sys.modules[self.MODULE_NAME])
                else:
                    importlib.import_module(self.MODULE_NAME)

        output = fake_out.getvalue()
        return output.strip().splitlines()

    def validateRegex(self, line: str) -> None:
        self.assertRegex(line, REGEX_FOR_LETTERS, "The print must contain a sentence explaining the result.")

    def test_odd(self):
        lines = self.run_exercise(11)
        print(lines)
        odd = lines[0].lower().__contains__("impar")
        m = re.search(REGEX_FOR_INT_WITHOUT_COLON, lines[0])
        self.assertIsNotNone(m)
        self.assertTrue(odd)
        self.validateRegex(lines[0])

    def test_even(self):
        lines = self.run_exercise(10)
        print(lines)
        even = lines[0].lower().__contains__(" par")
        m = re.search(REGEX_FOR_INT_WITHOUT_COLON, lines[0])
        self.assertIsNotNone(m)
        self.assertTrue(even)
        self.validateRegex(lines[0])

if __name__ == '__main__':
    unittest.main()
