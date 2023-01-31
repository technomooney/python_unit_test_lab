import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_string_list(self):
        items = ['test', 'string', 'lists']
        expected_discount = None
        returned_value = discount(items)
        self.assertEqual(expected_discount,returned_value)

    
    # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()