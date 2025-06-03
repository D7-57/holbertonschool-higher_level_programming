#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -2, -30]), -2)

    def test_mixed_sign_numbers(self):
        self.assertEqual(max_integer([-1, 0, 5, -3]), 5)

    def test_duplicates(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_max_at_start(self):
        self.assertEqual(max_integer([100, 1, 2]), 100)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 500]), 500)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_strings(self):
        self.assertEqual(max_integer("abc"), 'c')

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "zebra"]), "zebra")
