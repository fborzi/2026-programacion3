import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from test.utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_STRING


class TestExercise9(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio9"

    def run_exercise(self, *inputs) -> list[str]:
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

    def test_user_password_maria(self):
        lines = self.run_exercise("BORZI, FRANCO", 37122843, "BORZI, LUCIO", 37122800, "GARCÍA, MARÍA VERÓNICA", 37122844)
        print(lines)
        user1 = re.search(REGEX_FOR_STRING, lines[0])
        pass1 = re.search(REGEX_FOR_STRING, lines[1])
        user2 = re.search(REGEX_FOR_STRING, lines[2])
        pass2 = re.search(REGEX_FOR_STRING, lines[3])
        self.assertIsNotNone(user1)
        self.assertIsNotNone(pass1)
        self.assertIsNotNone(user2)
        self.assertIsNotNone(pass2)
        self.assertEqual(user1.group(0).strip(), "francoborzi")
        self.assertEqual(pass1.group(0).strip(), "2843")
        self.assertEqual(user2.group(0).strip(), "lucioborzi")
        self.assertEqual(pass2.group(0).strip(), "2800")
        self.validateRegex(lines[0])
        self.validateRegex(lines[1])
        self.validateRegex(lines[2])
        self.validateRegex(lines[3])

    def test_user_password_juan(self):
        lines = self.run_exercise("BORZI, ANTONIO", 37122843, "GARCÍA ÁLVAREZ, GINO", 37122800, "GARCÍA ÁLVAREZ, JUAN PABLO", 37122844)
        print(lines)
        user1 = re.search(REGEX_FOR_STRING, lines[0])
        pass1 = re.search(REGEX_FOR_STRING, lines[1])
        user2 = re.search(REGEX_FOR_STRING, lines[2])
        pass2 = re.search(REGEX_FOR_STRING, lines[3])
        self.assertIsNotNone(user1)
        self.assertIsNotNone(pass1)
        self.assertIsNotNone(user2)
        self.assertIsNotNone(pass2)
        self.assertEqual(user1.group(0).strip(), "antonioborzi")
        self.assertEqual(pass1.group(0).strip(), "2843")
        self.assertEqual(user2.group(0).strip(), "ginogarciaalvarez")
        self.assertEqual(pass2.group(0).strip(), "2800")
        self.validateRegex(lines[0])
        self.validateRegex(lines[1])
        self.validateRegex(lines[2])
        self.validateRegex(lines[3])

    def test_missing_input(self):
        with self.assertRaises(StopIteration):
            self.run_exercise("BORZI, FRANCO", 37122843, "BORZI, LUCIO", 37122800)

if __name__ == '__main__':
    unittest.main()
