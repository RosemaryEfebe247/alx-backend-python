#!/usr/bin/env python3
""" A class that tests multiple parameters"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ The class that inherits from unittest"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ The  method to test that the method
        returns what it is supposed to"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_error):
        """raise keyError for the following parameters"""
        with self.assertRaises(expected_error):
            access_nested_map(nested_map, path)
