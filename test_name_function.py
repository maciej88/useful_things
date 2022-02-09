import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""

    def test_first_last_name(self):
        """Data are supported?"""
        formtted_name = get_formatted_name('Frank', 'sinatra')
        self.assert_(formtted_name, 'Frank', 'Sinatra')

unittest.main()
