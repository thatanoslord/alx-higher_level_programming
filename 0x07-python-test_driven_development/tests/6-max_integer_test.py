#!/usr/bin/python3
"""Unittest for max_integer([..])

    Cases:
      - Empty List
      - String List
      - Single String
      - Float List
      - List of strings, integers and floats
      - Single Element List
      - Tuple
      - dictionary
      - List of Lists
      - Empty string
      - Ordered List
      - Unordered List

"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Definition of unit tests for max_integer([...])."""

    def test_empty(self):
        """Test for passing an empty list"""
        res = max_integer([])
        self.assertEqual(res, None)

    def test_string_list(self):
        """Test floating list"""
        res = max_integer(['tony', 'awad', 'ibrahim'])
        self.assertEqual(res, 'tony')

    def test_singleString(self):
        """ Test for string """
        res = max_integer("TONY")
        self.assertEqual(res, "Y")

    def test_floatList(self):
        """ Test for float list"""
        res = max_integer([1.2, 2.4, 8.9])
        self.assertEqual(res, 8.9)

    def test_complexList(self):
        """ Test for complex list"""
        self.assertRaises(TypeError, max_integer, [2, 3.9, "Tony"])

    def test_single(self):
        """ Test for single element list"""
        res = max_integer([9])
        self.assertEqual(res, 9)

    def test_tuple(self):
        """ Test for tuple"""
        res = max_integer((2, 9, 1))
        self.assertEqual(res, 9)

    def test_dict(self):
        """ Test for dictionary"""
        variable = {"first": 1, "second": 2}
        self.assertRaises(KeyError, max_integer, variable)

    def test_matrix(self):
        """ Test for matrix """
        res = max_integer([[4, 5, 6], [3, 4, 5]])
        self.assertEqual(res, [4, 5, 6])

    def test_emptyString(self):
        """ Test for empty string """
        res = max_integer("")
        self.assertEqual(res, None)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 8, 4, 3]
        self.assertEqual(max_integer(unordered), 8)


if __name__ == '__main__':
    """main function
    """
    unittest.main()
