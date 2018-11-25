import unittest
from format_price import format_price


class FomatPriceTest(unittest.TestCase):
    def test_int_price(self):
        price = format_price(1278)
        self.assertEqual(price, '1 278')

    def test_int_str_price(self):
        price = format_price('1278')
        self.assertEqual(price, '1 278')

    def test_int_price(self):
        price = format_price('1250000')
        self.assertEqual(price, '1 250 000')

    def test_float_price(self):
        price = format_price('2354.0000')
        self.assertEqual(price, '2 354')

    def test_correct_price(self):
        price = format_price('3 657')
        self.assertEqual(price, '3 657')

    def test_float__kop(self):
        price = format_price('0.1')
        self.assertEqual(price, '0.10')

    def test_float__kop_nozero(self):
        price = format_price('.1')
        self.assertEqual(price, '0.10')

    def test_backspaced_price(self):
        price = format_price(' 3657.578 ')
        self.assertEqual(price, '3 657.58')

    def test_price_with_letters(self):
        self.assertIsNone(format_price('817t36.5634'))
        self.assertIsNone(format_price(' zfg# 817t36.5634 '))
        self.assertIsNone(format_price('price'))

    def test_price_with_points(self):
        self.assertIsNone(format_price('8.3656.34'))
        self.assertIsNone(format_price('2.338.3656.34'))

    def test_price_with_special_chars(self):
        self.assertIsNone(format_price('3-36'))
        self.assertIsNone(format_price('3?36'))
        self.assertIsNone(format_price(' 3+36 '))
        self.assertIsNone(format_price('"3-36"'))
        self.assertIsNone(format_price('3#36#'))

    def test_price_with_comma(self):
        self.assertIsNone(format_price('3657,356'))
        self.assertIsNone(format_price('3,657.356'))

    def test_incorrect_type(self):
        self.assertIsNone(format_price(list()))
        self.assertIsNone(format_price(dict()))
        self.assertIsNone(format_price(tuple()))
        self.assertIsNone(format_price(set()))
        self.assertIsNone(format_price(True))
        self.assertIsNone(format_price(False))


if __name__ == '__main__':
    unittest.main()
