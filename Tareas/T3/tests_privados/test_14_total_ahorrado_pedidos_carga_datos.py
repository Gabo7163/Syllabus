import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_14 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_contenido_pedidos, cargar_pizzas, total_ahorrado_pedidos



class TestTotalAhorradoPedidosCargaDatos(unittest.TestCase):

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

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = total_ahorrado_pedidos(g_pe, g_pi)

        resultado_esperado = TOTAL_AHORRADO_PEDIDOS_S

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = total_ahorrado_pedidos(g_pe, g_pi)

        resultado_esperado = TOTAL_AHORRADO_PEDIDOS_S

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = total_ahorrado_pedidos(g_pe, g_pi)

        resultado_esperado = TOTAL_AHORRADO_PEDIDOS_M

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = total_ahorrado_pedidos(g_pe, g_pi)

        resultado_esperado = TOTAL_AHORRADO_PEDIDOS_M

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = total_ahorrado_pedidos(g_pe, g_pi)

        resultado_esperado = TOTAL_AHORRADO_PEDIDOS_M

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = total_ahorrado_pedidos(g_pe, g_pi)

        resultado_esperado = TOTAL_AHORRADO_PEDIDOS_L

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = total_ahorrado_pedidos(g_pe, g_pi)

        resultado_esperado = TOTAL_AHORRADO_PEDIDOS_L

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = total_ahorrado_pedidos(g_pe, g_pi)

        resultado_esperado = TOTAL_AHORRADO_PEDIDOS_L

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = total_ahorrado_pedidos(g_pe, g_pi)

        resultado_esperado = TOTAL_AHORRADO_PEDIDOS_L

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)
