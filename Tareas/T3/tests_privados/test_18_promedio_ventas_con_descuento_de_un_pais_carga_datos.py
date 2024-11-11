import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_18 import *
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_contenido_pedidos, cargar_pedidos, cargar_locales, \
    promedio_ventas_con_descuento_de_un_pais



class TestPromedioVentasConDescuentoDeUnPaisCargaDatos(unittest.TestCase):

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

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "locales.csv")
        g_l = cargar_locales(path)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            g_pe, g_as, g_l, "Germany"
        )

        resultado_esperado = PROMEDIO_VENTAS_CON_DESCUENTO_DE_UN_PAIS_S_1

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "locales.csv")
        g_l = cargar_locales(path)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            g_pe, g_as, g_l, "Somalia"
        )

        resultado_esperado = PROMEDIO_VENTAS_CON_DESCUENTO_DE_UN_PAIS_S_2

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "locales.csv")
        g_l = cargar_locales(path)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            g_pe, g_as, g_l, "Chile"
        )

        resultado_esperado = PROMEDIO_VENTAS_CON_DESCUENTO_DE_UN_PAIS_M_1

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "locales.csv")
        g_l = cargar_locales(path)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            g_pe, g_as, g_l, "French Polynesia"
        )

        resultado_esperado = PROMEDIO_VENTAS_CON_DESCUENTO_DE_UN_PAIS_M_2

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data_tests_privados", carpeta, "locales.csv")
        g_l = cargar_locales(path)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            g_pe, g_as, g_l, "Panama"
        )

        resultado_esperado = PROMEDIO_VENTAS_CON_DESCUENTO_DE_UN_PAIS_M_3

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)
