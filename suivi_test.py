# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:53:49 2016

@author: jessicahoffmann
"""

import unittest
from suivi import *
import os
import os.path 

class Goal_T(unittest.TestCase):

    def test_init_delete(self):
        g1 = Goal("a")
        g1.delete
        
        g2 = Goal("a")
        self.assertTrue(g1.address) 
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()