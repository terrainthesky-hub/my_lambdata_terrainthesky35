import unittest
from my_lambdata.datetimeextractor import DateTimeExtractor
import pandas as pd

class datechecker(unittest.TestCase):
    def test_month(self):
        x = ({'Date': "12-13-2001"})
        x = pd.DataFrame(x)
        DateTimeExtractor(x).datetimeconversion()
        breakpoint()
        self.assertEqual(month, 12)

