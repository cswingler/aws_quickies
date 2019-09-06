from unittest import TestCase

import control
from pprint import pprint as pp
from test.resources import *


class TestAControl(TestCase):


    def setUp(self):
        self.c = control.AControl()

    def test_find_instances(self):
        r = self.c.find_instances('sentry')
        pp(r)

        self.assertIsInstance(r, list)

    def test_filter_instance_data_human(self):
        r = self.c.filter_instance_data_human(instances)
        pp(r)

        self.assertIsInstance(r, list)

