import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from test.utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_INT_ONLY


class TestExercise3(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio3"

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

    def test_positives_even(self):
        lines = self.run_exercise(11, 2, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20)
        print(lines)
        odd = lines[0].lower().__contains__("8")
        m = re.search(REGEX_FOR_INT_ONLY, lines[0])
        self.assertIsNotNone(m)
        self.assertTrue(odd)
        self.validateRegex(lines[0])

    def test_negatives_even(self):
        lines = self.run_exercise(-11, -2, -4, 5, -6, -7, -8, -9, -10, -12, -14, -16, -20)
        print(lines)
        odd = lines[0].lower().__contains__("0")
        m = re.search(REGEX_FOR_INT_ONLY, lines[0])
        self.assertIsNotNone(m)
        self.assertTrue(odd)
        self.validateRegex(lines[0])

    def test_both_even(self):
        lines = self.run_exercise(-11, 2, 4, 5, 6, -7, -8, -9, -10, -12, 14, -16, -20)
        print(lines)
        odd = lines[0].lower().__contains__("4")
        m = re.search(REGEX_FOR_INT_ONLY, lines[0])
        self.assertIsNotNone(m)
        self.assertTrue(odd)
        self.validateRegex(lines[0])

    def test_missing_input(self):
        with self.assertRaises(StopIteration):
            self.run_exercise(5, 1, 2, 3, 4)

if __name__ == '__main__':
    unittest.main()
