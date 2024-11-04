import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_privados.timeout_function import timeout
from por_copiar.utilidades import N_SECOND
sys.stdout = open(os.devnull, 'w')

from consultas import promedio_ventas_con_descuento_de_un_pais



class TestPromedioVentasConDescuentoDeUnPaisCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione cuando no haya pedidos en tal país.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie Tunnel Apt. 363",
                pais="Afganistan",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks",
                pais="France",
                ciudad="North Trevor",
                cantidad_trabajadores=9,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Argentina",
                ciudad="Buenos Aires",
                cantidad_trabajadores=2,
            ),
            Local(
                id_local=4,
                direccion="Calle Falsa 126",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=4,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Suecia",
                ciudad="Stockholm",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.13
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.14
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.20
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.16
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiana_M", cantidad=6, descuento=0.12
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=2, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=4, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=3, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=5, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_locales,
            "Canada",
        )

        resultado_esperado = 0

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione cuando no haya descuentos en los pedidos del país.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie Tunnel Apt. 363",
                pais="Afganistan",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks",
                pais="France",
                ciudad="North Trevor",
                cantidad_trabajadores=9,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Argentina",
                ciudad="Buenos Aires",
                cantidad_trabajadores=2,
            ),
            Local(
                id_local=4,
                direccion="Calle Falsa 126",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=4,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Suecia",
                ciudad="Stockholm",
                cantidad_trabajadores=2,
            ),
        ]


        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.25
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.10
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.20
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiana_M", cantidad=6, descuento=0.13
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=2, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=4, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=5, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_locales,
            "Argentina",
        )

        resultado_esperado = 0

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione cuando haya descuentos en todos los pedidos del país.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie Tunnel Apt. 363",
                pais="Afganistan",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks",
                pais="France",
                ciudad="North Trevor",
                cantidad_trabajadores=9,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="France",
                ciudad="Paris",
                cantidad_trabajadores=2,
            ),
            Local(
                id_local=4,
                direccion="Calle Falsa 126",
                pais="France",
                ciudad="Marseille",
                cantidad_trabajadores=4,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Suecia",
                ciudad="Stockholm",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.12
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.16
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiana_M", cantidad=6, descuento=0.13
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=2, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=4, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=5, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_locales,
            "France",
        )

        resultado_esperado = 0.26

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione cuando haya más de una pizza por pedido.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie Tunnel Apt. 363",
                pais="Uruguay",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks",
                pais="Uruguay",
                ciudad="North Trevor",
                cantidad_trabajadores=9,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Uruguay",
                ciudad="Santiago",
                cantidad_trabajadores=6,
            ),
            Local(
                id_local=4,
                direccion="Calle Falsa 126",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=4,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Argentina",
                ciudad="Santiago",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiana_M", cantidad=2, descuento=0.13
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=12, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=5, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=6, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=15, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Pepperoni Clásica_M", cantidad=7, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Pepperoni Clásica_M", cantidad=7, descuento=0.28
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Napolitana_M", cantidad=9, descuento=0.28
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita pesto_S", cantidad=10, descuento=0.28
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Margarita_M", cantidad=8, descuento=0.17
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=2, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=4, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=5, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=3, id_cliente=7, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=4, id_cliente=8, fecha="2021-01-01", hora="12:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_locales,
            "Uruguay",
        )

        resultado_esperado = 0.26

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione si la mayoría de los pedidos tienen descuento y alguno más de una pizza.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie Tunnel Apt. 363",
                pais="Slovenia",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=9,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Slovenia",
                ciudad="Santiago",
                cantidad_trabajadores=6,
            ),
            Local(
                id_local=4,
                direccion="Calle Falsa 126",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=4,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Hawaiana_M", cantidad=6, descuento=0.1
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Pepperoni Clásica_M", cantidad=7, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.38
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Napolitana_M", cantidad=7, descuento=0.38
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita pesto_S", cantidad=8, descuento=0.38
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Margarita_M", cantidad=8, descuento=0.7
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=2, id_local=2, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=4, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=5, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=3, id_cliente=7, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=4, id_cliente=8, fecha="2021-01-01", hora="12:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = promedio_ventas_con_descuento_de_un_pais(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_locales,
            "Slovenia",
        )

        resultado_esperado = 0.38

        self.assertIsInstance(resultado_estudiante, (float))

        self.assertEqual(resultado_estudiante, resultado_esperado)
