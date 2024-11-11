import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_07 import *
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_pizzas, pizzas_con_ingrediente



class TestPizzaConIngredianteCargaDatos(unittest.TestCase):

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
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "queso")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_S_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "salsa BBQ")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "aceitunas negras")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "Salsa de Queso")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "Palta")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "champiñones")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "salsa de queso")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "Cerebro con Queso")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_L_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "Larvas Crujientes")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_L_4

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_p = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_p, "Cerebro con Queso")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_XL_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
