import os
import unittest
from collections.abc import Iterable
import sys
from tests_privados.timeout_function import timeout
from tests_privados.solution.test_03 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_contenido_pedidos, pedido_con_mayor_descuento_utilizado



class TestPedidoConMayorDescuentoUtilizadoCargaDatos(unittest.TestCase):

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

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_S[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_S[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_S[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_S[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_M[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_M[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_M[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_M[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_M[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_M[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_L[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_L[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_L[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_L[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_L[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_L[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_L[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_L[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedido_con_mayor_descuento_utilizado(g_pe)

        resultado_esperado, largo_esperado = (
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_XL[0],
            PEDIDO_CON_MAYOR_DESCUENTO_UTILIZADO_XL[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)
