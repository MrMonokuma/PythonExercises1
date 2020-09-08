import unittest

from Cadena import primeraUltima

class MyTestCase(unittest.TestCase):
    def test_primeraUltima(self):
        palabra1 = "azucar"
        self.assertEqual("a r", primeraUltima(palabra1))
        print("La primera y la última letra de su palabra son respectivamente: ", primeraUltima(palabra1))

if __name__ == '__main__':
    unittest.main()