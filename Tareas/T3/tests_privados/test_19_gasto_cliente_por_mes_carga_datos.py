import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_19 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_contenido_pedidos, cargar_pedidos, cargar_pizzas, \
    gasto_cliente_por_mes



class TestGastoClientePorMesCargaDatos(unittest.TestCase):

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
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = gasto_cliente_por_mes(
            g_pe, g_as, g_pi, 49, 2024)

        resultado_esperado = GASTO_CLIENTE_POR_MES_S_1

        self.assertIsInstance(resultado_estudiante, (list))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = gasto_cliente_por_mes(
            g_pe, g_as, g_pi, 41, 2024)

        resultado_esperado = GASTO_CLIENTE_POR_MES_S_2

        self.assertIsInstance(resultado_estudiante, (list))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = gasto_cliente_por_mes(
            g_pe, g_as, g_pi, 430, 2024)

        resultado_esperado = GASTO_CLIENTE_POR_MES_M_1

        self.assertIsInstance(resultado_estudiante, (list))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = gasto_cliente_por_mes(
            g_pe, g_as, g_pi, 66, 2024)

        resultado_esperado = GASTO_CLIENTE_POR_MES_M_2

        self.assertIsInstance(resultado_estudiante, (list))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = gasto_cliente_por_mes(
            g_pe, g_as, g_pi, 401, 2024)

        resultado_esperado = GASTO_CLIENTE_POR_MES_M_3

        self.assertIsInstance(resultado_estudiante, (list))

        self.assertEqual(resultado_estudiante, resultado_esperado)
