import unittest
from temp_converter import convert_celsius_to_fahrenheit

class TempConverterTest(unittest.TestCase):
    # Given temp in Celsius, convert temp to Fahrenheit.
    def test_celsius_is_converted_to_fahrenheit(self):
        fahr = convert_celsius_to_fahrenheit(20)
        self.assertEqual(fahr, 68, 
        "Should correctly convert Celsius to Fahrenheit")
        
if __name__ == '__main__':
    unittest.main()
