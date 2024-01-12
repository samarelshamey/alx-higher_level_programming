#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''
    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    
