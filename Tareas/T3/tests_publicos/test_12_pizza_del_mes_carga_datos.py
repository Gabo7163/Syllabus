import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_12 import *
from utilidades import N_SECOND

from consultas import cargar_contenido_pedidos, cargar_pedidos, pizza_del_mes



class TestPizzaDelMesCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_del_mes(g_as, g_pe, "01")

        resultado_esperado, largo_esperado = (
            TODAS_LAS_PIZZAS_DEL_MES_S_1[0],
            TODAS_LAS_PIZZAS_DEL_MES_S_1[1],
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

        path = os.path.join("data", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_del_mes(g_as, g_pe, "02")

        resultado_esperado, largo_esperado = (
            TODAS_LAS_PIZZAS_DEL_MES_S_2[0],
            TODAS_LAS_PIZZAS_DEL_MES_S_2[1],
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

        path = os.path.join("data", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_del_mes(g_as, g_pe, "01")

        resultado_esperado, largo_esperado = (
            TODAS_LAS_PIZZAS_DEL_MES_M_1[0],
            TODAS_LAS_PIZZAS_DEL_MES_M_1[1],
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

        path = os.path.join("data", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_del_mes(g_as, g_pe, "02")

        resultado_esperado, largo_esperado = (
            TODAS_LAS_PIZZAS_DEL_MES_M_2[0],
            TODAS_LAS_PIZZAS_DEL_MES_M_2[1],
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

        path = os.path.join("data", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_del_mes(g_as, g_pe, "03")

        resultado_esperado, largo_esperado = (
            TODAS_LAS_PIZZAS_DEL_MES_M_3[0],
            TODAS_LAS_PIZZAS_DEL_MES_M_3[1],
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

        path = os.path.join("data", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_del_mes(g_as, g_pe, "01")

        resultado_esperado, largo_esperado = (
            TODAS_LAS_PIZZAS_DEL_MES_L_1[0],
            TODAS_LAS_PIZZAS_DEL_MES_L_1[1],
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

        path = os.path.join("data", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_del_mes(g_as, g_pe, "02")

        resultado_esperado, largo_esperado = (
            TODAS_LAS_PIZZAS_DEL_MES_L_2[0],
            TODAS_LAS_PIZZAS_DEL_MES_L_2[1],
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

        path = os.path.join("data", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_del_mes(g_as, g_pe, "03")

        resultado_esperado, largo_esperado = (
            TODAS_LAS_PIZZAS_DEL_MES_L_3[0],
            TODAS_LAS_PIZZAS_DEL_MES_L_3[1],
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

        path = os.path.join("data", carpeta, "pedidos.csv")
        g_as = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_del_mes(g_as, g_pe, "04")

        resultado_esperado, largo_esperado = (
            TODAS_LAS_PIZZAS_DEL_MES_L_4[0],
            TODAS_LAS_PIZZAS_DEL_MES_L_4[1],
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        resultado_estudiante = list(resultado_estudiante)

        self.assertTrue(
            all(elem in resultado_estudiante for elem in resultado_esperado)
        )

        largo_estudiante = len(resultado_estudiante)

        self.assertEqual(largo_estudiante, largo_esperado)
