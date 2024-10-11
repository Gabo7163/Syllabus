import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import local_mas_pizzas_vendidas_por_tipo_de_pizza



class TestLocalMasPizzasVendidasPorTipoDePizzaCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando ese tipo de pizza no se vendió en ningún local.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_XL", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones bajo ajo_S", cantidad=30, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=1, fecha="2021-04-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=8, id_cliente=4, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2010-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
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
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=64,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Chile",
                ciudad="Valdivia",
                cantidad_trabajadores=131,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
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
                direccion="Calle Falsa 123427",
                pais="Chile",
                ciudad="Vina del Mar",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (
            asociacion for asociacion in lista_entregada)

        resultado_estudiante = local_mas_pizzas_vendidas_por_tipo_de_pizza(
            generador_entregado_pedidos,
            generador_entregado_asociaciones,
            generador_entregado_locales,
            "Pepe Hawaiiana",
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [local for local in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando solamente un local vendió más pizzas del tipo.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=4, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_XL", cantidad=10, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=43, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones bajo ajo_S", cantidad=30, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Vegetariana Normal_XL", cantidad=390, descuento=0.0
            ),
        ]

        generador_entregado_pedidos = (pedido for pedido in lista_entregada)

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-29", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=2, id_cliente=1, fecha="2021-04-05", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=6, id_cliente=4, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=4, id_cliente=5, fecha="2010-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=5, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
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
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=64,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Chile",
                ciudad="Valdivia",
                cantidad_trabajadores=131,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
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
                direccion="Calle Falsa 123427",
                pais="Chile",
                ciudad="Vina del Mar",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (
            asociacion for asociacion in lista_entregada)

        resultado_estudiante = local_mas_pizzas_vendidas_por_tipo_de_pizza(
            generador_entregado_pedidos,
            generador_entregado_asociaciones,
            generador_entregado_locales,
            "Vegetariana Normal",
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [local for local in resultado_estudiante]

        lista_esperada = [
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Ecuador",
                ciudad="Quito",
                cantidad_trabajadores=2546,
            )
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando hay empate en dos locales que vendieron igual cantidad de pizzas del tipo.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=250, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_XL", cantidad=250, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana Normal_M", cantidad=43, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones bajo ajo_S", cantidad=30, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásica_L", cantidad=500, descuento=0.0
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
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-05-07", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=6, id_cliente=4, fecha="2022-02-03", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=4, id_cliente=5, fecha="2010-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=2, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
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
                direccion="Calle Falsa 123427",
                pais="Chile",
                ciudad="Vina del Mar",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (
            asociacion for asociacion in lista_entregada)

        resultado_estudiante = local_mas_pizzas_vendidas_por_tipo_de_pizza(
            generador_entregado_pedidos,
            generador_entregado_asociaciones,
            generador_entregado_locales,
            "Pepperoni Clásica",
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [local for local in resultado_estudiante]

        lista_esperada = [
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=643,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North T revor",
                cantidad_trabajadores=1,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando hay empate en tres o más locales que vendieron igual cantidad de pizzas del tipo.
        """
        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pizza del Saber_S", cantidad=250, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_XL", cantidad=250, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Pizza del Saber_XL", cantidad=3000, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepe Hawaiiana_M", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pizza del Saber_M", cantidad=3000, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6,
                nombre="Pepperoni Clásica_L",
                cantidad=5089890,
                descuento=0.0,
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Pizza del Saber_S", cantidad=1500, descuento=0.0
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

        resultado_estudiante = local_mas_pizzas_vendidas_por_tipo_de_pizza(
            generador_entregado_pedidos,
            generador_entregado_asociaciones,
            generador_entregado_locales,
            "Pizza del Saber",
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [local for local in resultado_estudiante]

        lista_esperada = [
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Chile",
                ciudad="Valdivi",
                cantidad_trabajadores=131,
            ),
            Local(
                id_local=7,
                direccion="Calle Falsa 1.22474487139",
                pais="Chile",
                ciudad="Vina Mar del Vina 2.0",
                cantidad_trabajadores=200,
            ),
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Uzbekistan",
                ciudad="DARK SOULS",
                cantidad_trabajadores=10293,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
