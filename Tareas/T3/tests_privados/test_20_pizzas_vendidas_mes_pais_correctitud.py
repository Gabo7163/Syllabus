import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import pizzas_vendidas_mes_pais


class TestPizzasVendidasMesPaisCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando no se vendió ninguna pizza en el mes determinado en el país determinado.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pizza SUS_S", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni De Clásica_XL", cantidad=250, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Pizza del Saber_XL", cantidad=30030, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe Hawaiiana_M", cantidad=23, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pizza del Saber_M", cantidad=3000, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6,
                nombre="Pepperoni Clásica_L",
                cantidad=10,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Pizza del Saber_S", cantidad=15300, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pizza del Saber_L", cantidad=1498, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Pizza del Saber_M", cantidad=2, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=3, id_cliente=1, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=3, id_cliente=1, fecha="2021-04-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=4, id_cliente=3, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=6, id_cliente=4, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2010-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=5, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=7, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=7, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=9, id_local=7, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Uzbekistan",
                ciudad="DARK SOULS",
                cantidad_trabajadores=10293,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North T revor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=643,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Chile",
                ciudad="Valdivi",
                cantidad_trabajadores=131,
            ),
            Local(
                id_local=5,
                direccion="Calle NO Falsa 127",
                pais="Ecuador",
                ciudad="Quito",
                cantidad_trabajadores=2546,
            ),
            Local(
                id_local=6,
                direccion="Cal el 213",
                pais="Croacia",
                ciudad="FAs",
                cantidad_trabajadores=23213,
            ),
            Local(
                id_local=7,
                direccion="Calle Falsa 1.22474487139",
                pais="Chile",
                ciudad="Vina Mar del Vina 2.0",
                cantidad_trabajadores=200,
            ),
        ]

        generador_entregado_locales = (
            asociacion for asociacion in lista_entregada)

        int_estudiante = pizzas_vendidas_mes_pais(
            generador_entregado_pedidos,
            generador_entregado_asociaciones,
            generador_entregado_locales,
            "Ecuador",
            3,
            2021,
        )

        self.assertIsInstance(int_estudiante, int)

        int_esperado = 0

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando se vendió solamente una pizza en el mes determinado en el país determinado.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pizza Dudosa_S", cantidad=133, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="SLOTH oo.3_XL", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Pizza del Saber_XL", cantidad=3000, descuento=0.7
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe Neko_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pizz Saber_M", cantidad=3000, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6,
                nombre="Pepperoni Clásica_L",
                cantidad=5089890,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Mega Aqua JuaN_S", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pizza TAKIS_L", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Pizza del Saber_M", cantidad=1, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=3, id_cliente=1, fecha="2022-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=3, id_cliente=1, fecha="2022-04-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=4, id_cliente=3, fecha="2022-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=6, id_cliente=4, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2022-02-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=5, id_cliente=6, fecha="2022-02-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=7, id_cliente=6, fecha="2022-02-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=7, id_cliente=6, fecha="2022-02-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=9, id_local=7, id_cliente=6, fecha="2022-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Land of the Lustrous",
                ciudad="DARK SOULS",
                cantidad_trabajadores=10293,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North T revor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Land of the Lustrous",
                ciudad="Santiago",
                cantidad_trabajadores=643,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Chile",
                ciudad="Valdivi",
                cantidad_trabajadores=131,
            ),
            Local(
                id_local=5,
                direccion="Calle NO Falsa 127",
                pais="Land of the Lustrous",
                ciudad="Quitoed",
                cantidad_trabajadores=2546,
            ),
            Local(
                id_local=6,
                direccion="Cal el 213",
                pais="Land of the Lustrous",
                ciudad="FAs",
                cantidad_trabajadores=23213,
            ),
            Local(
                id_local=7,
                direccion="Calle Falsa 1.22474487139",
                pais="Land of the Lustrous",
                ciudad="Vina Mar del Vina 2.0",
                cantidad_trabajadores=200,
            ),
        ]

        generador_entregado_locales = (
            asociacion for asociacion in lista_entregada)

        int_estudiante = pizzas_vendidas_mes_pais(
            generador_entregado_pedidos,
            generador_entregado_asociaciones,
            generador_entregado_locales,
            "Land of the Lustrous",
            4,
            2022,
        )

        self.assertIsInstance(int_estudiante, int)

        int_esperado = 1

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando se vendieron dos o más pizzas en el mes determinado en el país determinado.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pizza JEFFre_S", cantidad=145445, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Nicole_XL", cantidad=25635645356, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Pizza Jecka DELTA_XL", cantidad=32, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe Neko_S", cantidad=6412, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pizz Saber_M", cantidad=3562, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=6,
                nombre="Bernkastel_L",
                cantidad=9512742,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=7,
                nombre="Mega Mega Witch of Truth_S",
                cantidad=41451222,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pizza SODA_L", cantidad=62, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Pizza IMC Saber_M", cantidad=3316, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=3, id_cliente=1, fecha="2030-04-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=3, id_cliente=1, fecha="2032-04-06", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=4, id_cliente=3, fecha="2032-04-07", hora="17:00:01"
            ),
            Pedido(
                id_pedido=4, id_local=6, id_cliente=4, fecha="2022-07-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2022-05-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=5, id_cliente=6, fecha="2032-04-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=7, id_cliente=6, fecha="2032-04-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=6, id_cliente=6, fecha="2022-04-01", hora="13:00:10"
            ),
            Pedido(
                id_pedido=9, id_local=6, id_cliente=6, fecha="2032-01-25", hora="13:30:00"
            ),
        ]

        generador_entregado_asociaciones = (
            asociacion for asociacion in lista_entregada
        )
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel AptKASTEL 23 Of Wisdom",
                pais="Rokkenjima",
                ciudad="DARK SOULS",
                cantidad_trabajadores=10293,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines LEAK VALGRIN",
                pais="Slovenia",
                ciudad="North T revor (Never is Never)",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Ari",
                pais="Pais de las Maravillas",
                ciudad="Silk Song City (NEVER COMING OUT)",
                cantidad_trabajadores=643,
            ),
            Local(
                id_local=4,
                direccion="Calle Tinkke 1618033988",
                pais="Childe",
                ciudad="ANGE",
                cantidad_trabajadores=131,
            ),
            Local(
                id_local=5,
                direccion="Calle Jecka 127",
                pais="Rokkenjima",
                ciudad="Quito",
                cantidad_trabajadores=2546,
            ),
            Local(
                id_local=6,
                direccion="Cal el 213",
                pais="Rokkenjima",
                ciudad="FAs",
                cantidad_trabajadores=23213,
            ),
            Local(
                id_local=7,
                direccion="Calle Falsa 1.22474487139",
                pais="Rokkenjima",
                ciudad="Vi4.0 ACHIEVEMENT EDIrTION",
                cantidad_trabajadores=20031,
            ),
        ]

        generador_entregado_locales = (
            asociacion for asociacion in lista_entregada)

        int_estudiante = pizzas_vendidas_mes_pais(
            generador_entregado_pedidos,
            generador_entregado_asociaciones,
            generador_entregado_locales,
            "Rokkenjima",
            4,
            2032,
        )

        self.assertIsInstance(int_estudiante, int)

        int_esperado = 50963964

        self.assertEqual(int_estudiante, int_esperado)
