import unittest

from ICE3_Owen.ICE3.src.temperature_sensor import validate_temperature, process_temperatures


class TestTemp(unittest.TestCase):

    def test_temp_in_range(self):
        # Test on the boundary line min
        self.assertEqual(validate_temperature(-50), -50)
        # Test on the boundary line Max
        self.assertEqual(validate_temperature(150), 150)
        # Test with decimal
        self.assertEqual(validate_temperature(20.5), 20.5)

    def test_temp_out_range(self):
        # Test lower then minimum
        self.assertEqual(validate_temperature(-51),"Not within valid range")
        # Test higher then maximum
        self.assertEqual(validate_temperature(151), "Not within valid range")

    def test_temp_invalid(self):
        # Invalid input
        temp_list = ["Hey"]
        self.assertRaises(Exception, process_temperatures(temp_list))

    def test_process_boundary(self):
        # Check multiple near boundary integers
        temp_list = [-49, 149]
        self.assertEqual(process_temperatures(temp_list), "Min: -49.0°C, Max: 149.0°C, Avg: 50.0°C")
    def test_process_invalid_input(self):
        # Check multiple inputs with invalid input
        temp_list = [-60, 20, 160]
        self.assertEqual(process_temperatures(temp_list), "Not within valid range")
    def test_process_string_input(self):
        # Valid inputs with a string value
        temp_list = [20, "abc", 30]
        self.assertEqual(process_temperatures(temp_list),"Invalid input")
    def test_process_special_char(self):
        # With special characters
        temp_list = [10, "@", -40]
        self.assertRaises(Exception, process_temperatures(temp_list))
    def test_process_large_numbers(self):
        # Inputs with extremely large numbers
        temp_list = [2**31 - 1, -2**31]
        self.assertEqual(process_temperatures(temp_list),"Not within valid range")
    def test_process_same_inputs(self):
        # Completely even inputs
        temp_list = [50,50,50]
        self.assertEqual(process_temperatures(temp_list),"Min: 50.0°C, Max: 50.0°C, Avg: 50.0°C")
    def test_process_no_input(self):
        # No input
        temp_list = []
        self.assertEqual(process_temperatures(temp_list), "No valid input provided.")

