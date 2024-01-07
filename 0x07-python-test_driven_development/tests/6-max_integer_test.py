#!/usr/bin/python3
"""Unittest for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer"""
    def test_empty_list(self):
        """test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_arg(self):
        """test one argument"""
        self.assertEqual(max_integer([5]), 5)

    def test_no_arg(self):
        """test no arguments"""
        self.assertEqual(max_integer(), None)

    def test_normal(self):
        """test normal list"""
        self.assertEqual(max_integer([1, 4, 6, 7]), 7)

    def test_ordered(self):
        """test ordered list"""
        self.assertEqual(max_integer([1, 3, 5, 7, 8, 9, 12]), 12)

    def tes_unordered(self):
        """test unordered list"""
        self.assertEqual(max_integer([4, 1, 7, 0, 12, 6, 5]), 12)

    def test_same_elements(self):
        """test same elements"""
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

    def test_postive_and_negative(self):
        """test positive and negative elements"""
        self.assertEqual(max_integer([5, -1, 4, -3, -199, 500, 2, 0,
                                     333, 234, 9, 10, 89, 98, 108, -256]), 500)

    def test_negative(self):
        """test negative elements"""
        self.assertEqual(max_integer([-5, -1, -4, -3, -199, -500, -2, -340,
                                     -333, -234, -9, -10, -89, -98, -108,
                                     -256]), -1)

    def test_int_and_float(self):
        """test int and float"""
        self.assertEqual(max_integer(
                [10.34, 99.8, 100, -0.1, 3000, 9999, -200000, 9798.9]), 9999)

    def test_floats(self):
        """test float elements"""
        self.assertEqual(max_integer(
                             [2.367014439486981136, 1.2442932193120425423,
                                 1.269673745943177, 9.6021998063297004,
                                 0.040663644666581, 7.318418153098476,
                                 11.14782568486828354, 1.694150096609713,
                                 0.523292479047324, 12.577278388003499,
                                 0.03165696316739835, 40.8284765683928,
                                 13.9723205356754642, 1.0167973840532782,
                                 3.87655444444444, 14.17994528432150622,
                                 0.34268959203149724, 2.456678975543,
                                 15.8237893847200373, 6.564703466354198,
                                 0.650943204479027,
                                 16.8902940005294793, 7.691604865311827,
                                 8.897302744173896,
                                 17.0780411284398352, 1.6564018996809176,
                                 100.123456789000,
                                 19.7495378363397325, 0.6460418901123863,
                                 1.23345678987654,
                                 20.29656944388569284, 1.2020859950744733,
                                 12.34567876542,
                                 22.695758513783994, 0.37293339285604976,
                                 13.234567876542,
                                 10.8540047898304736, 0.16021193325291794,
                                 12.34567876542,
                                 10.027891891117170508, 0.8464685760135892,
                                 12.2345431232,
                                 14.506719557284897, 2.0258041087808,
                                 4.525163681550944,
                                 11.3277284362225874, 3.042753010712081,
                                 2.4201460936424986,
                                 10.6254206993310946, 3.6037820704785766,
                                 2.234543213456764,
                                 10.5843942753272469, 2.994055932449279,
                                 0.5168645505697169, 0.014982685631661026,
                                 0.02477737364433171]), 100.123456789000)

    def test_alpha_str(self):
        """test alphabetic string"""
        self.assertEqual(max_integer([["coo"], ["aoo"], ["abc"],
                                     ["sic"], ["ric"]]),  ["sic"])

    def test_numric_str(self):
        """test numeric string"""
        self.assertEqual(max_integer("1928234575444"), "9")

    def test_str(self):
        """test string"""
        self.assertEqual(max_integer("Elshamy"), "y")

    def test_list(self):
        """test list"""
        self.assertEqual(max_integer([[], [3], [4], [1, 8]]), [4])

    def test_nan(self):
        """test nan"""
        self.assertEqual(max_integer([50, float('nan'), 100]), 100)

    def test_none(self):
        """test none"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_infin(self):
        """test inf"""
        self.assertEqual(max_integer([88, float('inf'), float('-inf')]),
                         float('inf'))

    def test_dictionary(self):
        """test dictionary"""
        with self.assertRaises(TypeError):
            max_integer([{11: 2, 4: 5}, {"c": "l", "s": "a"}])

    def test_int(self):
        """test integer"""
        with self.assertRaises(TypeError):
            max_integer(100)

    def test_float(self):
        """test float"""
        with self.assertRaises(TypeError):
            max_integer(11.8)


if __name__ == '__main__':
    unittest.main()
