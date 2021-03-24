import unittest


class MyTestCase(unittest.TestCase):

    def test_basecase(self):
        lat, lng = -33.865143, 151.209900
        timestamp = 1480933800
        from Utils.timezone_converter_utils import convert_timestamp_with_coordinates
        time = convert_timestamp_with_coordinates(lat, lng, timestamp)

        self.assertEqual(time, '05/12/2016 21:30 AEDT +1100')

    def test_whole_csv_file_cases(self):
        from Utils.csv_file_parser import load_csv_to_df, add_converted_column_on_df

        df = load_csv_to_df()
        add_converted_column_on_df(df)

        target_result = ['16/04/2017 10:04 +10 +1000', '04/03/2003 07:45 +03 +0300', '07/07/2015 07:30 BST +0100',
                         '23/09/1998 22:48 +07 +0700', '11/03/2010 23:34 EAT +0300', '01/11/2013 06:05 GMT +0000',
                         '07/05/2007 21:51 SAST +0200', '25/08/2011 10:00 NZST +1200', '08/04/2016 06:12 AEST +1000',
                         '03/10/2012 18:27 CEST +0200', '02/06/2017 03:34 AEST +1000']

        for index, row in df.iterrows():
            self.assertEqual(row["local_time"], target_result[index])


if __name__ == '__main__':
    unittest.main()
