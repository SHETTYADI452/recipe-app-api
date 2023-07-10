"""
Sample Tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTestCase(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res =calc.add(5,6)

        self.assertEqual(res,11)