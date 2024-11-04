import unittest
from main import serializar_tortuga, encriptar
from main import deserializar_tortuga, desencriptar
from clases import Tortuga


class TestIntegracion(unittest.TestCase):

    def test_integracion_encriptar(self):
        """
        Verificar que todo el proceso de encriptar está bueno
        """
        test = encriptar(bytearray(b"\x00\x01\x02\x03\x0A"), 1, 3)
        res = bytearray(
            b"\x00\x00\x03\x03\x02\x01\x00\x00\x01\x02\x0A\x00\x00\x01\x00\x00\x03"
        )

        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_integracion_desencriptar(self):
        """
        Verificar que todo el proceso de desencriptar está bueno
        """
        test = desencriptar(
            bytearray(b"\x00\x00\x02\x04\x01\x03\x00\x00\x01\x00\x00\x02\x00\x00\x03")
        )

        res = bytearray(b"\x03\x00\x04\x01")
        self.assertIsInstance(test, bytearray)
        self.assertEqual(test, res)

    def test_integracion_todo_proceso(self):
        """
        Verificar que todo el proceso de encriptar y desencripar está bueno
        """
        original = Tortuga("Shion")
        original.celebrar_anivesario()
        serializado = serializar_tortuga(original)
        encriptado = encriptar(serializado, 3, 12)
        desencriptado = desencriptar(encriptado)
        deserializado = deserializar_tortuga(desencriptado)
        self.assertDictEqual(original.__dict__, deserializado.__dict__)

    def test_integracion_todo_proceso_2(self):
        """
        Verificar que todo el proceso de encriptar y desencripar está bueno
        """
        original = Tortuga("Pepa2.0")
        original.celebrar_anivesario()
        original.celebrar_anivesario()
        serializado = serializar_tortuga(original)
        encriptado = encriptar(serializado, 5, 21)
        desencriptado = desencriptar(encriptado)
        deserializado = deserializar_tortuga(desencriptado)
        self.assertDictEqual(original.__dict__, deserializado.__dict__)
