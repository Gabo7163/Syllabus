import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_17 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_contenido_pedidos, cargar_pedidos, cargar_pizzas, \
    ganancia_total_de_un_local



class TestGananciaTotalDeUnLocalCargaDatos(unittest.TestCase):

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

        resultado_estudiante = ganancia_total_de_un_local(g_pe, g_as, g_pi, 34)

        resultado_esperado = GANANCIA_TOTAL_DE_UN_LOCAL_S_1

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

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = ganancia_total_de_un_local(g_pe, g_as, g_pi, 20)

        resultado_esperado = GANANCIA_TOTAL_DE_UN_LOCAL_S_2

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

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = ganancia_total_de_un_local(g_pe, g_as, g_pi, 1)

        resultado_esperado = GANANCIA_TOTAL_DE_UN_LOCAL_M_1

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

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = ganancia_total_de_un_local(g_pe, g_as, g_pi, 6)

        resultado_esperado = GANANCIA_TOTAL_DE_UN_LOCAL_M_2

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

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = ganancia_total_de_un_local(g_pe, g_as, g_pi, 7)

        resultado_esperado = GANANCIA_TOTAL_DE_UN_LOCAL_M_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)
