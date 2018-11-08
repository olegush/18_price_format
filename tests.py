import unittest
from format_price import format_price


class FomatPriceTest(unittest.TestCase):
    def test_float_price(self):
        price = format_price('2354.0000')
        self.assertEqual(price, '2 354')

    def test_rub_kop_price(self):
        price = format_price('5436руб.80коп.')
        self.assertEqual(price, '5 437')

    def test_comma_price(self):
        price = format_price('3657,356')
        self.assertEqual(price, '3 657')

    def test_correct_price(self):
        price = format_price('3 657')
        self.assertEqual(price, '3 657')

    def test_float__rub_price(self):
        price = format_price(' 8736.000 руб.')
        self.assertEqual(price, '8 736')


if __name__ == '__main__':
    unittest.main()
