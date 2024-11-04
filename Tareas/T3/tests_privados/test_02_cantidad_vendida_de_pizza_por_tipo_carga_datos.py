import os
import sys
import unittest

from tests_privados.timeout_function import timeout
from tests_privados.solution.test_02 import *
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import cargar_contenido_pedidos, cantidad_vendida_de_pizza_por_tipo


class TestCantidadVendidaDePizzaPorTipoCargaDatos(unittest.TestCase):

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

        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Carnívora BBQ"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_S_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")

        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Pepinillos y Tocino"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_S_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Palta y Tomate"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_M_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Sublime Fino Sabroso con Cuidado"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_M_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Cremoso Tradicional Encantador con Encanto"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_M_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Fino Sublime Delicioso con Delicadeza"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_L_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Picante Crujiente Dorado con Dedicación"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_L_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Asombroso Crujiente Fresquito con Belleza"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_L_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Dorado Cálido Radiante con Calidez"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_L_4

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data_tests_privados", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Increíble Increíble Asombroso con Sabor"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_XL_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)
