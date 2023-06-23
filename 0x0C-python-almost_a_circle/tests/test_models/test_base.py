#!/usr/bin/python3
import unittest
import os
import sys
sys.path.append("..")

from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_save_to_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]

        s1 = Square(5)
        s2 = Square(9, 1, 3)
        list_squares = [s1, s2]

        Rectangle.save_to_file_csv(list_rectangles)
        Square.save_to_file_csv(list_squares)

        self.assertTrue(os.path.exists("Rectangle.csv"))
        self.assertTrue(os.path.exists("Square.csv"))

    def test_load_from_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]

        s1 = Square(5)
        s2 = Square(9, 1, 3)
        list_squares = [s1, s2]

        Rectangle.save_to_file_csv(list_rectangles)
        Square.save_to_file_csv(list_squares)

        loaded_rectangles = Rectangle.load_from_file_csv()
        loaded_squares = Square.load_from_file_csv()

        self.assertEqual(len(loaded_rectangles), len(list_rectangles))
        self.assertEqual(len(loaded_squares), len(list_squares))

        for rect1, rect2 in zip(list_rectangles, loaded_rectangles):
            self.assertEqual(rect1.__dict__, rect2.__dict__)

        for square1, square2 in zip(list_squares, loaded_squares):
            self.assertEqual(square1.__dict__, square2.__dict__)

if __name__ == '__main__':
    unittest.main()
