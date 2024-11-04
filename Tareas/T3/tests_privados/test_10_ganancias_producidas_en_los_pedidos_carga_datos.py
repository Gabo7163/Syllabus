import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_10 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_contenido_pedidos, cargar_pizzas, ganancias_producidas_en_los_pedidos



class TestGananciasProducidasEnLosPedidosCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(g_pe, g_pi)

        resultado_esperado = GANANCIAS_PRODUCIDAS_EN_LOS_PEDIDOS_S

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(g_pe, g_pi)

        resultado_esperado = GANANCIAS_PRODUCIDAS_EN_LOS_PEDIDOS_S

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(g_pe, g_pi)

        resultado_esperado = GANANCIAS_PRODUCIDAS_EN_LOS_PEDIDOS_M

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(g_pe, g_pi)

        resultado_esperado = GANANCIAS_PRODUCIDAS_EN_LOS_PEDIDOS_M

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(g_pe, g_pi)

        resultado_esperado = GANANCIAS_PRODUCIDAS_EN_LOS_PEDIDOS_M

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(g_pe, g_pi)

        resultado_esperado = GANANCIAS_PRODUCIDAS_EN_LOS_PEDIDOS_L

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(g_pe, g_pi)

        resultado_esperado = GANANCIAS_PRODUCIDAS_EN_LOS_PEDIDOS_L

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(g_pe, g_pi)

        resultado_esperado = GANANCIAS_PRODUCIDAS_EN_LOS_PEDIDOS_L

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pizzas.csv")
        g_pi = cargar_pizzas(path)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(g_pe, g_pi)

        resultado_esperado = GANANCIAS_PRODUCIDAS_EN_LOS_PEDIDOS_L

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
