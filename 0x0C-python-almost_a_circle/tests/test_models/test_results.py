#!/usr/bin/python3
import unittest
import os
import sys
sys.path.append("..")


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_base_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    # Add more tests for Rectangle methods

class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    # Add more tests for Square methods

if __name__ == '__main__':
    unittest.main()
