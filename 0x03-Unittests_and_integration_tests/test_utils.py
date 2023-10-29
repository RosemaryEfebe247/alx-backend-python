#!/usr/bin/env python3
""" A class that tests multiple parameters"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """ Use mock and patch to mimic a url"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        """ Test if the mock works"""
        mock_get = Mock()
        mock_get.json.return_value = test_payload
        with patch("utils.requests.get", return_value=mock_get):
            result = get_json(test_url)
            print(result)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)
