import unittest

from ParImpar import parImpar

class MyTestCase(unittest.TestCase):
    def test_parImpar(self):
        num1 = 3;
        self.assertEqual(False, parImpar(num1))
        print(parImpar(num1), '- El número ', num1, 'es impar')

if __name__ == '__main__':
    unittest.main()
