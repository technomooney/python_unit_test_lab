import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_seven_prices(self):
            prices = [54, 53, 94, 76, 27, 56, 91]
            expected_discount = 27
            self.assertEqual(expected_discount, discount(prices))

    def test_list_of_two_prices(self):
        prices = [10, 20]
        expected_discount = None
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_one_prices(self):
        prices = [10]
        expected_discount = None
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_twenty_prices(self):
        prices = [472, 712, 502, 382, 216, 968, 574, 22, 200, 367, 148, 942, 171, 745, 798, 571, 231, 651, 541, 801]
        expected_discount = 22
        self.assertEqual(expected_discount, discount(prices))

    def test_string_list(self):
        items = ['test', 'string', 'lists']
        expected_discount = None
        returned_value = discount(items)
        self.assertEqual(expected_discount,returned_value)
    
    def test_mixed_data_type(self):
        items = [2, "test", 2.4, False]
        expected_discount = None
        returned_value = discount(items)
        self.assertEqual(expected_discount,returned_value)


    

    # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()