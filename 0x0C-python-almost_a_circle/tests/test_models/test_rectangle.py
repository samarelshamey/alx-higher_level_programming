#!/usr/bin/python3
"""Module for Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io

class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_class(self):
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_constrcut(self):
        with self.assertRaises(TypeError) as exc:
            rec = Rectangle()
        strng = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(exc.exception), strng)

    def test_construct2(self):
        with self.assertRaises(TypeError) as exc:
            rec = Rectangle(5, 6, 7, 2, 4, 3)
        strng = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(exc.exception), strng)

    def test_construct3(self):
        with self.assertRaises(TypeError) as exc:
            rec = Rectangle(5)
        strng =  "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(exc.exception), strng)

    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_instantiation(self):
        rec = Rectangle(30, 10)
        self.assertEqual(str(type(rec)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(rec, Base))
        ar = {'_Rectangle__height': 10, '_Rectangle__width': 30,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rec.__dict__, ar)

        with self.assertRaises(TypeError) as exc:
            rec = Rectangle("6", 2)
        msg = "width must be an integer"
        self.assertEqual(str(exc.exception), msg)

        with self.assertRaises(TypeError) as exc:
            rec = Rectangle(1, "9")
        msg = "height must be an integer"
        self.assertEqual(str(exc.exception), msg)

        with self.assertRaises(TypeError) as exc:
            rec = Rectangle(1, 2, "4")
        msg = "x must be an integer"
        self.assertEqual(str(exc.exception), msg)

        with self.assertRaises(TypeError) as exc:
            rec = Rectangle(1, 2, 3, "5")
        msg = "y must be an integer"
        self.assertEqual(str(exc.exception), msg)

        with self.assertRaises(ValueError) as exc:
            rec = Rectangle(-7, 2)
        msg = "width must be > 0"
        self.assertEqual(str(exc.exception), msg)

        with self.assertRaises(ValueError) as exc:
            rec = Rectangle(1, -8)
        msg = "height must be > 0"
        self.assertEqual(str(exc.exception), msg)

        with self.assertRaises(ValueError) as exc:
            rec = Rectangle(0, 2)
        msg = "width must be > 0"
        self.assertEqual(str(exc.exception), msg)

        with self.assertRaises(ValueError) as exc:
            rec = Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertEqual(str(exc.exception), msg)

        with self.assertRaises(ValueError) as exc:
            rec = Rectangle(1, 2, -3)
        msg = "x must be >= 0"
        self.assertEqual(str(exc.exception), msg)

        with self.assertRaises(ValueError) as exc:
            rec = Rectangle(1, 2, 3, -4)
        msg = "y must be >= 0"
        self.assertEqual(str(exc.exception), msg)

        rec = Rectangle(9, 15, 30, 20)
        ar = {'_Rectangle__height': 15, '_Rectangle__width': 9,
             '_Rectangle__x': 30, '_Rectangle__y': 20, 'id': 12}
        self.assertEqual(rec.__dict__, ar)

        rec = Rectangle(5, 10, 15, 20, 98)
        ar = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(rec.__dict__, ar)

        rec = Rectangle(100, 200, id=510, y=99, x=101)
        ar = {'_Rectangle__height': 200, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 510}
        self.assertEqual(rec.__dict__, ar)

    def test_id(self):
        Base._Base__nb_objects = 77
        rec = Rectangle(3, 5)
        self.assertEqual(rec.id, 78)

    def test_properities(self):
        rec = Rectangle(7, 9)
        rec.width = 300
        rec.height = 200
        rec.x = 100
        rec.y = 105
        ar = {'_Rectangle__height': 200, '_Rectangle__width': 300,
             '_Rectangle__x': 100, '_Rectangle__y': 105, 'id': 1}
        self.assertEqual(rec.__dict__, ar)
        self.assertEqual(rec.width, 300)
        self.assertEqual(rec.height, 200)
        self.assertEqual(rec.x, 100)
        self.assertEqual(rec.y, 105)

    def invalid_types(self):
        typ = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
               [4], {5}, {6: 7}, None)
        return typ

    def test_type(self):
        rec = Rectangle(1, 2)
        attrs = ["x", "y", "width", "height"]
        for attr in attrs:
            strng = "{} must be an integer".format(attr)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as exc:
                    setattr(rec, attr, invalid_type)
                self.assertEqual(str(exc.exception), strng)

    def test_negative(self):
        rec = Rectangle(3, 5)
        attrs = ["width", "height"]
        for attr in attrs:
            strng = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as exc:
                setattr(rec, attr, -(randrange(10) + 1))
            self.assertEqual(str(exc.exception), strng)

    def test_nagative2(self):
        rec = Rectangle(3, 5)
        attrs = ["x", "y"]
        for attr in attrs:
            strng = "{} must be >= 0".format(attr)
            with self.assertRaises(ValueError) as exc:
                setattr(rec, attr, -(randrange(10) + 1))
            self.assertEqual(str(exc.exception), strng)

    def test_zero(self):
        rec = Rectangle(3, 5)
        attrs = ["width", "height"]
        for attr in attrs:
            strng = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as exc:
                setattr(rec, attr, 0)
            self.assertEqual(str(exc.exception), strng)

    def test_property(self):
        rec = Rectangle(1, 2)
        attrs = ["x", "y", "width", "height"]
        for attr in attrs:
            num = randrange(10) + 1
            setattr(rec, attr, num)
            self.assertEqual(getattr(rec, attr), num)

    def test_property2(self):
        rec = Rectangle(1, 2)
        rec.x = 0
        rec.y = 0
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)

    def test_area(self):
        rec = Rectangle(5, 6)
        with self.assertRaises(TypeError) as exc:
            Rectangle.area()
        strng = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(exc.exception), strng)

        rec = Rectangle(5, 6)
        self.assertEqual(rec.area(), 30)
        wid = randrange(10) + 1
        heigh = randrange(10) + 1
        rec.width = wid
        rec.height = heigh
        self.assertEqual(rec.area(), wid * heigh)
        w = randrange(10) + 1
        h = randrange(10) + 1
        rec = Rectangle(w, h, 7, 8, 9)
        self.assertEqual(rec.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        rec = Rectangle(w, h, y=7, x=8, id=9)
        self.assertEqual(rec.area(), w * h)

        rec1 = Rectangle(3, 2)
        self.assertEqual(rec1.area(), 6)

        rec2 = Rectangle(2, 10)
        self.assertEqual(rec2.area(), 20)

        rec3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rec3.area(), 56)

    def test_display(self):
        rec = Rectangle(9, 8)
        with self.assertRaises(TypeError) as exc:
            Rectangle.display()
        strng = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(exc.exception), strng)

    
    def test_display2(self):
        rec = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            rec.display()
        strng = "#\n"
        self.assertEqual(f.getvalue(), strng)
        rec.width = 3
        rec.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            rec.display()
        strng = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), strng)

        rec = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            rec.display()
        strng = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(f.getvalue(), strng)
        rec = Rectangle(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            rec.display()
        strng = """\
#########
#########
#########
#########
#########
#########
#########
#########
"""
        self.assertEqual(f.getvalue(), strng)

        rec = Rectangle(1, 1, 10, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            rec.display()
        strng = """\










          #
"""
        self.assertEqual(f.getvalue(), strng)

        rec = Rectangle(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            rec.display()
        strng = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), strng)

        rec = Rectangle(5, 3, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            rec.display()
        strng = """\
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), strng)

        rec = Rectangle(5, 3, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            rec.display()
        strng = """\




#####
#####
#####
"""
        self.assertEqual(f.getvalue(), strng)
