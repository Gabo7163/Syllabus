import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_04 import *
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_pizzas, ajustar_precio_segun_ingredientes


class TestAjustarPrecioSegunIngredientesCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "salsa de cebolla", 14281
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_S_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "jamón", 10430
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "queso azul", 0
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Sangre Coagulada", 1030
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Dedos Chamuscados", 1042
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Larvas Crujientes", 10324520
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "atún", -3100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Piel Marchita", 313
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_L_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Ojos de Gnomo", 100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_L_4

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "pera", 10350
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_XL_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
