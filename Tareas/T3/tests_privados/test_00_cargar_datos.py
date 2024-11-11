import os
import sys
import unittest
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from utilidades import Pizzas, Locales, ContenidoPedidos, Pedidos
from utilidades import N_SECOND

sys.stdout = open(os.devnull, "w")

from consultas import (
    cargar_pizzas,
    cargar_locales,
    cargar_pedidos,
    cargar_contenido_pedidos,
)


class TestCargarDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_l_pizzas(self):
        """
        Verifica que los datos carguen bien con un dataset L de Pizzas.
        """
        path = os.path.join("data_tests_privados", "l", "pizzas.csv")
        generador = cargar_pizzas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 14976)

        # Revisar posiciones aleatorias
        pizzas_cargadas = [
            generador[0],
            generador[152],
            generador[4231],
            generador[-1],
        ]

        pizzas_esperadas = [
            Pizzas(
                nombre="Crujiente Increíble Irresistible con Alegría_S",
                ingredientes="pepinillos;queso;Salsa BBQ;tomate;salsa de tomate",
                precio=8544,
            ),
            Pizzas(
                nombre="Tentador Exquisito Tentador con Amor_L",
                ingredientes="Escamas de Dragón;Dedos Chamuscados;salsa de pimienta",
                precio=19392,
            ),
            Pizzas(
                nombre="Fresco Salado Maravilloso con Perfección_M",
                ingredientes="pimiento;huevo;tomate cherry;salsa blanca",
                precio=12323,
            ),
            Pizzas(
                nombre="Jugoso Glorioso Irresistible con Fervor_L",
                ingredientes="Huevo;Corazón Desgarrado;Cerebro con Queso;choclo;salsa de mostaza",
                precio=19183,
            ),
        ]

        self.assertCountEqual(pizzas_cargadas, pizzas_esperadas)

    @timeout(N_SECOND)
    def test_xl_pizzas(self):
        """
        Verifica que los datos carguen bien con un dataset XL de Pizzas.
        """
        path = os.path.join("data_tests_privados", "xl", "pizzas.csv")
        generador = cargar_pizzas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 147639)

        # Revisar posiciones aleatorias
        pizzas_cargadas = [
            generador[0],
            generador[156],
            generador[2414],
            generador[-1],
        ]

        pizzas_esperadas = [
            Pizzas(
                nombre="Glorioso Irresistible Tierno con Cariño_S",
                ingredientes="Salsa Blanca;piña;salsa de tomate",
                precio=9821,
            ),
            Pizzas(
                nombre="Cremoso Brillante Fresquito con Virtud_S",
                ingredientes="Pulmones Fritos;jamón;salsa de champiñones",
                precio=9919,
            ),
            Pizzas(
                nombre="Tentador Tradicional Delicioso con Cariño_L",
                ingredientes="camarones;champiñones;salsa blanca",
                precio=16398,
            ),
            Pizzas(
                nombre="Aromático Perfecto Increíble con Nobleza_L",
                ingredientes="Pulmones Fritos;piña;salsa de pimienta",
                precio=16270,
            ),
        ]

        self.assertCountEqual(pizzas_cargadas, pizzas_esperadas)

    @timeout(N_SECOND)
    def test_l_locales(self):
        """
        Verifica que los datos carguen bien con un dataset L de Locales.
        """
        path = os.path.join("data_tests_privados", "l", "locales.csv")
        generador = cargar_locales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 40000)

        # Revisar posiciones aleatorias
        locales_cargados = [
            generador[0],
            generador[421],
            generador[3514],
            generador[-1],
        ]

        locales_esperados = [
            Locales(
                id_local=0,
                direccion="4183 John Fields Apt. 733 4183",
                pais="France",
                ciudad="Flowersport",
                cantidad_trabajadores=19,
            ),
            Locales(
                id_local=421,
                direccion="9140 Watkins Points Suite 512 9140",
                pais="Somalia",
                ciudad="Lake Matthew",
                cantidad_trabajadores=17,
            ),
            Locales(
                id_local=3514,
                direccion="154 Kristina Glen Suite 866 154",
                pais="Sweden",
                ciudad="Stacyport",
                cantidad_trabajadores=6,
            ),
            Locales(
                id_local=39999,
                direccion="0648 Burns Meadows Suite 764 0648",
                pais="Malta",
                ciudad="North Hollyville",
                cantidad_trabajadores=4,
            ),
        ]

        self.assertCountEqual(locales_cargados, locales_esperados)

    @timeout(N_SECOND)
    def test_xl_locales(self):
        """
        Verifica que los datos carguen bien con un dataset XL de Locales.
        """
        path = os.path.join("data_tests_privados", "xl", "locales.csv")
        generador = cargar_locales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 400000)

        # Revisar posiciones aleatorias
        locales_cargados = [
            generador[0],
            generador[2356],
            generador[9721],
            generador[-1],
        ]

        locales_esperados = [
            Locales(
                id_local=0,
                direccion="409 Cook Drive 409",
                pais="South Georgia and the South Sandwich Islands",
                ciudad="North Sandra",
                cantidad_trabajadores=15,
            ),
            Locales(
                id_local=2356,
                direccion="USS Mason USS",
                pais="Belize",
                ciudad="Lake Kathleen",
                cantidad_trabajadores=4,
            ),
            Locales(
                id_local=9721,
                direccion="28343 Brenda Ford Suite 297 28343",
                pais="San Marino",
                ciudad="West Georgeland",
                cantidad_trabajadores=9,
            ),
            Locales(
                id_local=399999,
                direccion="12121 Thomas Club Suite 551 12121",
                pais="Norfolk Island",
                ciudad="West Nicole",
                cantidad_trabajadores=17,
            ),
        ]

        self.assertCountEqual(locales_cargados, locales_esperados)

    @timeout(N_SECOND)
    def test_l_contenido_pedidos(self):
        """
        Verifica que los datos carguen bien con un dataset L de ContenidoPedidos.
        """
        path = os.path.join("data_tests_privados", "l", "contenido_pedidos.csv")
        generador = cargar_contenido_pedidos(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 174925)

        # Revisar posiciones aleatorias
        contenido_cargado = [
            generador[0],
            generador[7324],
            generador[5322],
            generador[-1],
        ]

        contenido_esperado = [
            ContenidoPedidos(
                id_pedido=0,
                nombre="Brillante Picante Encantador con Toque Divino_S",
                cantidad=3,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=2939,
                nombre="Delicioso Glorioso Fresco con Frescura_S",
                cantidad=5,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=2118,
                nombre="Vibrante Fino Cremoso con Brío_L",
                cantidad=2,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=69997,
                nombre="Perfecto Maravilloso Esponjoso con Sutileza_L",
                cantidad=3,
                descuento=0.0,
            ),
        ]

        self.assertCountEqual(contenido_cargado, contenido_esperado)

    @timeout(N_SECOND)
    def test_xl_contenido_pedidos(self):
        """
        Verifica que los datos carguen bien con un dataset XL de ContenidoPedidos.
        """
        path = os.path.join("data_tests_privados", "xl", "contenido_pedidos.csv")
        generador = cargar_contenido_pedidos(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 1750014)

        # Revisar posiciones aleatorias
        contenido_cargado = [
            generador[0],
            generador[13625],
            generador[625],
            generador[-1],
        ]

        contenido_esperado = [
            ContenidoPedidos(
                id_pedido=0,
                nombre="Tradicional Sabroso Cremoso con Amor_M",
                cantidad=1,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=5412,
                nombre="Increíble Tentador Sabroso con Genialidad_M",
                cantidad=2,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=252,
                nombre="Suave Perfecto Tentador con Frescura_S",
                cantidad=5,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=699999,
                nombre="Aromático Increíble Glorioso con Arte_S",
                cantidad=3,
                descuento=0.0,
            ),
        ]

        self.assertCountEqual(contenido_cargado, contenido_esperado)

    @timeout(N_SECOND)
    def test_l_pedidos(self):
        """
        Verifica que los datos carguen bien con un dataset L de Pedidos.
        """
        path = os.path.join("data_tests_privados", "l", "pedidos.csv")
        generador = cargar_pedidos(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 70000)

        # Revisar posiciones aleatorias
        pedidos_cargados = [
            generador[0],
            generador[1574],
            generador[5766],
            generador[-1],
        ]

        pedidos_esperados = [
            Pedidos(
                id_pedido=0,
                id_local=28053,
                id_cliente=43110,
                fecha="2024-05-23",
                hora="23:51:57",
            ),
            Pedidos(
                id_pedido=1574,
                id_local=58,
                id_cliente=47783,
                fecha="2024-07-20",
                hora="10:19:41",
            ),
            Pedidos(
                id_pedido=5766,
                id_local=21814,
                id_cliente=26713,
                fecha="2024-08-14",
                hora="10:58:40",
            ),
            Pedidos(
                id_pedido=69999,
                id_local=29513,
                id_cliente=687,
                fecha="2024-09-13",
                hora="00:02:41",
            ),
        ]

        self.assertCountEqual(pedidos_cargados, pedidos_esperados)

    @timeout(N_SECOND)
    def test_xl_pedidos(self):
        """
        Verifica que los datos carguen bien con un dataset XL de Pedidos.
        """
        path = os.path.join("data_tests_privados", "xl", "pedidos.csv")
        generador = cargar_pedidos(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 700000)

        # Revisar posiciones aleatorias
        pedidos_cargados = [
            generador[0],
            generador[16232],
            generador[75413],
            generador[-1],
        ]

        pedidos_esperados = [
            Pedidos(
                id_pedido=0,
                id_local=66748,
                id_cliente=270463,
                fecha="2024-05-31",
                hora="00:35:55",
            ),
            Pedidos(
                id_pedido=16232,
                id_local=337676,
                id_cliente=199004,
                fecha="2024-04-01",
                hora="16:44:38",
            ),
            Pedidos(
                id_pedido=75413,
                id_local=77372,
                id_cliente=77638,
                fecha="2024-04-11",
                hora="08:52:57",
            ),
            Pedidos(
                id_pedido=699999,
                id_local=110372,
                id_cliente=437711,
                fecha="2024-07-12",
                hora="02:49:12",
            ),
        ]

        self.assertCountEqual(pedidos_cargados, pedidos_esperados)
