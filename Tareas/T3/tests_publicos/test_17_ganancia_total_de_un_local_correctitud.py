import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import ganancia_total_de_un_local



class TestGananciaTotalDeUnLocalCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que el local no tiene pedidos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

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
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
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
                id_pedido=2, id_local=1, id_cliente=2, fecha="2021-01-01", hora="12:30:00"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=3, fecha="2021-01-01", hora="17:00:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            2,
        )

        resultado_esperado = 0

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si es que el local tiene 3 pedidos con más de una pizza y descuentos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Vegetariana_M", cantidad=1, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
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
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:30:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=3, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
        )

        resultado_esperado = round(156008)

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si es que el local tiene 4 pedidos con más de una pizza y descuentos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Napolitana_S",
                ingredientes="tomate;queso;aceitunas;orégano",
                precio=12505,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Vegetariana_M", cantidad=1, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Napolitana_S", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
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
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:30:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
        )

        resultado_esperado = 159501

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione si hay 5 pedidos en el local.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Margarita_S",
                ingredientes="tomate;queso;salsa de tomate",
                precio=9050,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Vegetariana_M", cantidad=1, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=2, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Margarita_S", cantidad=4, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_S", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Vegetariana_M", cantidad=3, descuento=0.6
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
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:30:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=7, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=2, id_cliente=8, fecha="2021-01-01", hora="13:00:00"
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
        )

        resultado_esperado = 169835

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione si hay 6 pedidos en el local.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Margarita_S",
                ingredientes="tomate;queso;salsa de tomate",
                precio=9050,
            ),
            Pizza(
                nombre="Napolitana_S",
                ingredientes="tomate;queso;aceitunas;orégano",
                precio=12505,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Vegetariana_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=2, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Margarita_S", cantidad=4, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_S", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Napolitana_S", cantidad=5, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Napolitana_S", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Margarita_S", cantidad=3, descuento=0.6
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
                id_pedido=3, id_local=3, id_cliente=3, fecha="2021-01-01", hora="17:30:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=4, fecha="2021-01-01", hora="18:30:00"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=5, fecha="2021-01-01", hora="12:00:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=6, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=7, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=8, id_local=2, id_cliente=8, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=9, id_local=2, id_cliente=9, fecha="2021-01-01", hora="13:00:00"
            ),
            Pedido(
                id_pedido=10,
                id_local=1,
                id_cliente=10,
                fecha="2021-01-01",
                hora="13:00",
            ),
        ]

        generador_entregado_pedidos = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = ganancia_total_de_un_local(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
        )

        resultado_esperado = 270897

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual(resultado_estudiante, resultado_esperado)
