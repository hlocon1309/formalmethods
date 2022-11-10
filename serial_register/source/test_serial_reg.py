from unittest import TestCase
from serial_reg import serial_reg

class SerialRegTest(TestCase):

    def test_serial(self):
        self.assertEqual(serial_reg(0, 1, 1), True)