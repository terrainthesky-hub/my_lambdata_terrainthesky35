import unittest
from my_lambdata.datetimeextractor import DateTimeExtractor
import pandas as pd

class datechecker(unittest.TestCase):
    def month_tester(self):
        x = ({'Date': "12-13-2001"})
        x = pd.DataFrame(x)
        DateTimeExtractor(x).datetimeconversion()
        self.assertEqual(month, 12)