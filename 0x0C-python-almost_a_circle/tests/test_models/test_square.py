#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    """Tests the square class"""

    def setUp(self):
        """Instantiates class"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up """
        pass

    def test_class(self):
        """Tests Square class"""
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_inheritance(self):
        """Tests inherits from Base"""
        self.assertTrue(issubclass(Square, Base))

    def test_constructor(self):
        """Tests constructor"""
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_constructor2(self):
        """Tests constructor"""
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(e.exception), s)

    def test_instantiation(self):
        """Tests instantiation"""
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_instantiation2(self):
        """Tests instantiation"""
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(r.__dict__, d)

    def test_instantiation3(self):
        """Tests instantiation"""
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_id(self):
        """Tests if id is inherited from Base"""
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_properties(self):
        """Tests property"""
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    def invalid_types(self):
        """Returns tuple of types for validation"""
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_type(self):
        """Tests property validation"""
        r = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(r, "width", invalid_type)
            self.assertEqual(str(e.exception), s)

    def test_negative(self):
        """Tests property"""
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_negative2(self):
        """Tests property"""
        r = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_zero(self):
        """Tests property"""
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_property(self):
        """Tests property"""
        r = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_propertyzero(self):
        """Tests property"""
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_area(self):
        """Tests area() method"""
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_area2(self):
        """Tests area() method"""
        r = Square(6)
        self.assertEqual(r.area(), 36)
        w = randrange(10) + 1
        r.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, 7, 8, 9)
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * w)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_display(self):
        """Tests display() method"""
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_display2(self):
        """Tests display() method"""
        r = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.size = 3
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Square(5, 6, 7)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(1, 1, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\










 #
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 3)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s2.display()
        s = """\
  ##
  ##
"""
        self.assertEqual(f.getvalue(), s)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        s = """\



 ###
 ###
 ###
"""
        self.assertEqual(f.getvalue(), s)

    def test_str(self):
        """Tests __str__() method"""
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_str2(self):
        """Tests __str__() method"""
        r = Square(5)
        s = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(r), s)
        r = Square(1, 1)
        s = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(r), s)
        r = Square(3, 4, 5)
        s = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(r), s)
        r = Square(10, 20, 30, 40)
        s = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(r), s)

    def test_update_args(self):
        """Tests update"""
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_update(self):
        """Tests update"""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(10, 5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_update2(self):
        """Tests update"""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(ValueError) as e:
            r.update(10, -5)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, -17)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, 17, -25)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    def test_update3(self):
        """Tests update"""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(size=17)
        d["_Rectangle__height"] = 17
        d["_Rectangle__width"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_update4(self):
        """Tests update"""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5, x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5, x=20, y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

        r.update(y=25, id=10, x=20, size=5)
        self.assertEqual(r.__dict__, d)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")
