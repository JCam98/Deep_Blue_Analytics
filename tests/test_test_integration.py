"""
Description: The purpose of this module is to perform automated
unit tests for test_integration.py
"""
import unittest
from src.test_integration import Dummy

class TestDummy(unittest.TestCase):
    """Test suite for the Dummy class."""
    def setUp(self):
        """Set up a common Dummy object for tests."""
        self.dummy_obj = Dummy(10)
        self.dummy_obj_1 = Dummy(5)
        self.none_obj = Dummy(None)
    
    # --- Expected/Nominal Behavior ---
    def test_calc_x_2(self):
        """ Testing expected behavior of calc_x_2 """
        self.assertEqual(self.dummy_obj.calc_x_2(), 100)
        self.assertEqual(self.dummy_obj_1.calc_x_2(), 25)
    

    # --- Edge Cases ---

    def test_none_values(self):
        """Test with None as values."""
        self.assertIsNone(self.none_obj.x)
        self.assertEqual(self.none_obj.x, None)

    # --- Error Handling ---

    def test_calc_x_2_incorrect_dtype(self):
        """Test that set_vals raises TypeError with incorrect argument type."""
        with self.assertRaises(TypeError):
            self.dummy_obj.calc_x_2("1")
            
if __name__ == '__main__':
    unittest.main()