import unittest
from my_lambdata.datetimeextractor import DateTimeExtractor
import pandas as pd

class datechecker(unittest.TestCase):
    def test_month(self):
        data = ['12-08-2012']
        df = pd.DataFrame(data, columns=['Date'])
        year, month, day, df2 = DateTimeExtractor(df['Date']).datetimeconversion()
        print(month)
        self.assertEqual(month[0], 12)