from django.test import TestCase
from .models import Categoria, MarcaVehiculo, ModeloVehiculo, Pedido


class CategoriaTest(TestCase):
    def test_nombre_categoria(self):
        categoria = Categoria.objects.create(nombre="Repuestos")
        self.assertEqual(str(categoria), "Repuestos")
        self.assertTrue(categoria.activa)


class VehiculoTest(TestCase):
    def test_nombre_marca(self):
        marca = MarcaVehiculo.objects.create(nombre="Toyota")
        self.assertEqual(str(marca), "Toyota")

    def test_representacion_modelo(self):
        marca = MarcaVehiculo.objects.create(nombre="Toyota")
        modelo = ModeloVehiculo.objects.create(
            marca_vehiculo=marca,
            nombre="Corolla",
            año_inicio=2020,
        )
        self.assertEqual(
            str(modelo),
            "Toyota Corolla (2020-presente)"
        )


class PedidoTest(TestCase):
    def test_estado_predeterminado(self):
        pedido = Pedido.objects.create(
            order_id="TEST123",
            email="test@example.com",
            monto=10000,
        )
        self.assertEqual(pedido.estado, "pendiente")
