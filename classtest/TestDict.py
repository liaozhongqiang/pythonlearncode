#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import unittest
from classtest.mydict import Dict


class MyTestCase(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b=2)
        self.assertEqual(d.a, 1)

    if __name__ == '__main__':
        unittest.main()
