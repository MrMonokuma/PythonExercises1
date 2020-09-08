import unittest

from Descuento import descuentoProducto

class MyTestCase(unittest.TestCase):
    def test_descuentoProducto(self):
        precio1 = 10000;
        dia1 = "l"
        self.assertEqual(9000, descuentoProducto(dia1,precio1))
        print("El precio total de su producto es: ", descuentoProducto(dia1, precio1), "$")

if __name__ == '__main__':
    unittest.main()