import unittest
import json
import os
from Utils.csv_file_parser import load_csv_to_df
from startup import create_app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app("test")
        self.app = app.test_client()

    def test_get_all_response_status(self):
        response = self.app.get('/api/1.0/time-converter/all', )
        self.assertTrue(response.status_code, 200)

    def test_get_all(self):
        response = self.app.get('/api/1.0/time-converter/all', )
        data = {
            "0": "16/04/2017 10:04 +10 +1000",
            "12": "02/06/2017 03:34 AEST +1000",
            "162": "03/10/2012 18:27 CEST +0200",
            "23": "04/03/2003 07:45 +03 +0300",
            "274": "11/03/2010 23:34 EAT +0300",
            "27a1": "07/05/2007 21:51 SAST +0200",
            "73": "01/11/2013 06:05 GMT +0000",
            "73k": "08/04/2016 06:12 AEST +1000",
            "741": "25/08/2011 10:00 NZST +1200",
            "826": "23/09/1998 22:48 +07 +0700",
            "92": "07/07/2015 07:30 BST +0100"
        }

        self.assertTrue(response.data, json.dumps(data))

    def test_get_id_status(self):
        response = self.app.get('/api/1.0/time-converter/73k', )
        self.assertTrue(response.status_code, 200)

    def test_get_id(self):
        response = self.app.get('/api/1.0/time-converter/73k', )
        data = {"73k": "08/04/2016 06:12 AEST +1000", }
        self.assertTrue(response.data, json.dumps(data))

    def test_post_succcessful_id_status(self):
        response = self.app.post(
            '/api/1.0/time-converter/add/?id=1&lat=-33.865143&lng=151.209900&timestamp=1480933800', )
        self.assertTrue(response.status_code, 201)

    def test_post_succcessful(self):
        ''' need to delete timezone_modified.csv first'''
        if os.path.exists('../input_csv_files/timezone_modified.csv'):
            os.remove('../input_csv_files/timezone_modified.csv')

        original_df = load_csv_to_df('../input_csv_files/timezone.csv')

        if not os.path.exists('../input_csv_files/timezone_modified.csv'):
            response = self.app.post(
                '/api/1.0/time-converter/add/?id=1&lat=-33.865143&lng=151.209900&timestamp=1480933800', )

            after_post_df = load_csv_to_df('../input_csv_files/timezone_modified.csv')

            self.assertTrue(len(original_df), len(after_post_df) - 1)

    def test_post_fail_id_status(self):
        response = self.app.post(
            '/api/1.0/time-converter/add/?id=0&lat=-33.865143&lng=151.209900&timestamp=1480933800', )
        self.assertTrue(response.status_code, 404)

    def test_post_fail(self):
        ''' need to delete timezone_modified.csv first'''
        if os.path.exists('../input_csv_files/timezone_modified.csv'):
            os.remove('../input_csv_files/timezone_modified.csv')

        original_df = load_csv_to_df('../input_csv_files/timezone.csv')

        if not os.path.exists('../input_csv_files/timezone_modified.csv'):
            response = self.app.post(
                '/api/1.0/time-converter/add/?id=0&lat=-33.865143&lng=151.209900&timestamp=1480933800', )

            after_post_df = load_csv_to_df('../input_csv_files/timezone_modified.csv')

            self.assertTrue(len(original_df), len(after_post_df))

    def test_put_update(self):
        response = self.app.put('/api/1.0/time-converter/0/?lat=-33.865143&lng=151.209900&timestamp=1480933800', )
        data = {"status": "successful updated all", }
        self.assertTrue(response.data, json.dumps(data))

    def test_put_create(self):
        response = self.app.put('/api/1.0/time-converter/99/?lat=-33.865143&lng=151.209900&timestamp=1480933800', )
        data = {"status": "successful create new", }
        self.assertTrue(response.data, json.dumps(data))

    def test_delete_successful_status(self):
        response = self.app.delete('/api/1.0/time-converter/0', )
        data = {"status": "successful delete", }
        self.assertTrue(response.data, json.dumps(data))

    def test_delete_succcessful(self):
        ''' need to delete timezone_modified.csv first'''
        if os.path.exists('../input_csv_files/timezone_modified.csv'):
            os.remove('../input_csv_files/timezone_modified.csv')
        original_df = load_csv_to_df('../input_csv_files/timezone.csv')

        if not os.path.exists('../input_csv_files/timezone_modified.csv'):
            response = self.app.delete('/api/1.0/time-converter/0', )
            after_delete_df = load_csv_to_df('../input_csv_files/timezone_modified.csv')

            self.assertTrue(len(original_df), len(after_delete_df) + 1)

    def test_delete_fail_status(self):
        response = self.app.delete('/api/1.0/time-converter/9527', )
        data = {"error": "Not found", }
        self.assertTrue(response.data, json.dumps(data))

    def test_delete_fail(self):
        ''' need to delete timezone_modified.csv first'''
        if os.path.exists('../input_csv_files/timezone_modified.csv'):
            os.remove('../input_csv_files/timezone_modified.csv')

        original_df = load_csv_to_df('../input_csv_files/timezone.csv')

        if not os.path.exists('../input_csv_files/timezone_modified.csv'):
            response = self.app.delete('/api/1.0/time-converter/9527', )

            after_delete_df = load_csv_to_df('../input_csv_files/timezone_modified.csv')

        self.assertTrue(len(original_df), len(after_delete_df))


if __name__ == '__main__':
    unittest.main()
