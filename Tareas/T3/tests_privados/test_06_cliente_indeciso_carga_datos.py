import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_06 import *
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_pizzas, cliente_indeciso


class TestClienteIndecisoCargaDatos(unittest.TestCase):

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "salsa de pimentón", 17
        )

        resultado_esperado = CLIENTE_INDECISO_S_1

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

        resultado_estudiante = cliente_indeciso(generador_pizzas, "tocino", 453)

        resultado_esperado = CLIENTE_INDECISO_S_2

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

        resultado_estudiante = cliente_indeciso(generador_pizzas, "tomate cherry", 67)

        resultado_esperado = CLIENTE_INDECISO_M_1

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

        resultado_estudiante = cliente_indeciso(generador_pizzas, "rúcula", 98)

        resultado_esperado = CLIENTE_INDECISO_M_2

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "Trozos de Cerebro", 364
        )

        resultado_esperado = CLIENTE_INDECISO_M_3

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "Sangre Coagulada", 60
        )

        resultado_esperado = CLIENTE_INDECISO_L_1

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

        resultado_estudiante = cliente_indeciso(generador_pizzas, "Moco de Momia", 41)

        resultado_esperado = CLIENTE_INDECISO_L_2

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "Hígado Descompuesto", 3052
        )

        resultado_esperado = CLIENTE_INDECISO_L_3

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "Ojos de Gnomos", 4942
        )

        resultado_esperado = CLIENTE_INDECISO_L_4

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

        resultado_estudiante = cliente_indeciso(generador_pizzas, "Piel Marchita", 442)

        resultado_esperado = CLIENTE_INDECISO_XL_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
