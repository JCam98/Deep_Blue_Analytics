"""
Description: The purpose of this module is to perform automated
unit tests for input.py
"""
import unittest
import io
import sys
from src.input import Input


class TestInput(unittest.TestCase):
    """Test suite for the Input class."""

    def setUp(self):
        """Set up a common Input object for tests."""
        self.input_obj = Input(10, 20)

    # --- Expected/Nominal Behavior ---

    def test_initialization(self):
        """Test that the object is initialized with the correct values."""
        self.assertEqual(self.input_obj.x, 10)
        self.assertEqual(self.input_obj.y, 20)

    def test_set_vals(self):
        """Test that set_vals correctly updates the attributes."""
        self.input_obj.set_vals(100, 200)
        self.assertEqual(self.input_obj.x, 100)
        self.assertEqual(self.input_obj.y, 200)

    def test_get_vals(self):
        """Test that get_vals prints the correct output."""
        captured_output = io.StringIO()
        sys.stdout = captured_output  # Redirect stdout
        self.input_obj.get_vals()
        sys.stdout = sys.__stdout__  # Reset stdout
        self.assertEqual(captured_output.getvalue().strip(), "10 20")

        # Test again after changing values
        self.input_obj.set_vals(55, 77)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.input_obj.get_vals()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "55 77")

    # --- Edge Cases ---

    def test_different_numeric_types(self):
        """Test initialization and setting with floats and negative numbers."""
        float_obj = Input(-5.5, 0.0)
        self.assertEqual(float_obj.x, -5.5)
        self.assertEqual(float_obj.y, 0.0)

    def test_non_numeric_types(self):
        """Test with string values."""
        string_obj = Input("hello", "world")
        self.assertEqual(string_obj.x, "hello")
        self.assertEqual(string_obj.y, "world")

    def test_none_values(self):
        """Test with None as values."""
        none_obj = Input(None, 15)
        self.assertIsNone(none_obj.x)
        self.assertEqual(none_obj.y, 15)
        none_obj.set_vals(30, None)
        self.assertEqual(none_obj.x, 30)
        self.assertIsNone(none_obj.y)

    # --- Error Handling ---

    def test_set_vals_one_argument(self):
        """Test that set_vals raises TypeError with incorrect arguments."""
        with self.assertRaises(TypeError):
            self.input_obj.set_vals(1)
    def test_set_vals_string_args(self):
        """ Test that set_vals raises TypeError with incorrect (string) arguments. """
        with self.assertRaises(TypeError):
            self.input_obj.set_vals("1", "2")
    def test_set_vals_mismatching_args(self):
        """ Test that set_vals raises TypeError with one correct and one incorrect argument"""
        with self.assertRaises(TypeError):
            self.input_obj.set_vals("1", 1)

if __name__ == '__main__':
    unittest.main()
