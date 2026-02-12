import importlib
import re
import unittest
import io
import sys
from unittest.mock import patch

from src.ejercicios.funciones import es_par, suma_digitos, mostrar_suma_digitos, maximo, usuario, contrasenia_por_defecto, titulo
from test.utils.constant import REGEX_FOR_INT_ONLY


class TestFunciones(unittest.TestCase):
    def test_es_par(self):
        self.assertTrue(es_par(2))
        self.assertTrue(es_par(0))
        self.assertFalse(es_par(1))
        self.assertFalse(es_par(-1))

    def test_suma_digitos(self):
        self.assertEqual(suma_digitos(123), 6)
        self.assertEqual(suma_digitos(0), 0)
        self.assertEqual(suma_digitos(-999), 0)

    def test_mostrar_suma_digitos(self):
        with patch("sys.stdout", new = io.StringIO()) as fake_out:
            mostrar_suma_digitos(123)

        output = fake_out.getvalue().strip()
        number = re.search(REGEX_FOR_INT_ONLY, output)
        self.assertEqual(number.group(0).strip(), "6")

    def test_maximo(self):
        self.assertEqual(maximo(5, 10), 10)
        self.assertEqual(maximo(-5, -10), 10)
        self.assertEqual(maximo(0, 0), 0)

    def test_usuario(self):
        self.assertEqual(usuario("GARCÍA, MARÍA VERÓNICA"), "mariaveronicagarcia")
        self.assertEqual(usuario("BORZI, FRANCO"), "francoborzi")
        self.assertEqual(usuario("GARCÍA ÁLVAREZ, JUAN PABLO"), "juanpablogarciaalvarez")

    def test_contrasenia_por_defecto(self):
        self.assertEqual(contrasenia_por_defecto(37122843), "2843")
        self.assertEqual(contrasenia_por_defecto(12345678), "5678")
        self.assertEqual(contrasenia_por_defecto(2345000), "5000")

    def test_titulo(self):
        self.assertEqual(titulo("esto es una prueba"), "esto es una prueba".title())
        self.assertEqual(titulo("FRANCO BORZI"), "FRANCO BORZI".title())
        self.assertEqual(titulo("hARRY pOTTER y lA pIEDRA fILOSOFAL"), "hARRY pOTTER y lA pIEDRA fILOSOFAL".title())