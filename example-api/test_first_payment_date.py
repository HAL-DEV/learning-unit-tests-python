from unittest import TestCase

import datetime

from main import first_payment_date, MONTHLY, FORTNIGHTLY


class TestFirstDatePayment(TestCase):

    def test_monthly(self):
        self.assertEqual(datetime.datetime.strptime("2020-11-06", '%Y-%m-%d').date(),
                         first_payment_date("2020-10-06", MONTHLY))

    def test_fortnightly(self):
        self.assertEqual(datetime.datetime.strptime("2020-03-15", '%Y-%m-%d').date(),
                         first_payment_date("2020-03-11", FORTNIGHTLY))
        self.assertEqual(datetime.datetime.strptime("2020-04-15", '%Y-%m-%d').date(),
                         first_payment_date("2020-04-09", FORTNIGHTLY))
        self.assertEqual(datetime.datetime.strptime("2020-02-29", '%Y-%m-%d').date(),
                         first_payment_date("2020-02-22", FORTNIGHTLY))
        self.assertEqual(datetime.datetime.strptime("2020-10-31", '%Y-%m-%d').date(),
                         first_payment_date("2020-10-29", FORTNIGHTLY))
