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
        """setup"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """teardown"""
        pass

    def test_class(self):
        """test class type"""
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_constrcut(self):
        """test construct"""
        with self.assertRaises(TypeError) as exc:
            rec = Rectangle()
        strng = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(exc.exception), strng)

    def test_construct2(self):
        """test construct"""
        with self.assertRaises(TypeError) as exc:
            rec = Rectangle(5, 6, 7, 2, 4, 3)
        strng = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(exc.exception), strng)

    def test_construct3(self):
        """test construct"""
        with self.assertRaises(TypeError) as exc:
            rec = Rectangle(5)
        strng =  "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(exc.exception), strng)

    def test_inheritance(self):
        """test inheritance"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_instantiation(self):
        """test instantiation"""
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
             '_Rectangle__x': 30, '_Rectangle__y': 20, 'id': 2}
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
        """test id"""
        Base._Base__nb_objects = 77
        rec = Rectangle(3, 5)
        self.assertEqual(rec.id, 78)

    def test_properities(self):
        """test porperty"""
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
        """test types"""
        typ = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
               [4], {5}, {6: 7}, None)
        return typ

    def test_type(self):
        """test type"""
        rec = Rectangle(1, 2)
        attrs = ["x", "y", "width", "height"]
        for attr in attrs:
            strng = "{} must be an integer".format(attr)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as exc:
                    setattr(rec, attr, invalid_type)
                self.assertEqual(str(exc.exception), strng)

    def test_negative(self):
        """test negative"""
        rec = Rectangle(3, 5)
        attrs = ["width", "height"]
        for attr in attrs:
            strng = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as exc:
                setattr(rec, attr, -(randrange(10) + 1))
            self.assertEqual(str(exc.exception), strng)

    def test_nagative2(self):
        """test negative"""
        rec = Rectangle(3, 5)
        attrs = ["x", "y"]
        for attr in attrs:
            strng = "{} must be >= 0".format(attr)
            with self.assertRaises(ValueError) as exc:
                setattr(rec, attr, -(randrange(10) + 1))
            self.assertEqual(str(exc.exception), strng)

    def test_zero(self):
        """test zero"""
        rec = Rectangle(3, 5)
        attrs = ["width", "height"]
        for attr in attrs:
            strng = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as exc:
                setattr(rec, attr, 0)
            self.assertEqual(str(exc.exception), strng)

    def test_property(self):
        """test property"""
        rec = Rectangle(1, 2)
        attrs = ["x", "y", "width", "height"]
        for attr in attrs:
            num = randrange(10) + 1
            setattr(rec, attr, num)
            self.assertEqual(getattr(rec, attr), num)

    def test_property2(self):
        """test property"""
        rec = Rectangle(1, 2)
        rec.x = 0
        rec.y = 0
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)

    def test_area(self):
        """test area method"""
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
        """test display"""
        rec = Rectangle(9, 8)
        with self.assertRaises(TypeError) as exc:
            Rectangle.display()
        strng = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(exc.exception), strng)

    
    def test_display2(self):
        """test display"""
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

    def test_no_args(self):
        """test no arguments"""
        rec = Rectangle(5, 2)
        with self.assertRaises(TypeError) as exc:
            Rectangle.__str__()
        strng = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(exc.exception), strng)

    def test_str(self):
        """test string"""
        rec = Rectangle(5, 2)
        strng = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(rec), strng)

        rec = Rectangle(1, 1, 1)
        strng = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(rec), strng)

        rec = Rectangle(3, 4, 5, 6)
        strng = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(rec), strng)

        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rec1), "[Rectangle] (12) 2/1 - 4/6")

        rec2 = Rectangle(5, 5, 1)
        self.assertEqual(str(rec2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        """test update method"""
        rec = Rectangle(5, 2)
        with self.assertRaises(TypeError) as exc:
            Rectangle.update()
        strng = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(exc.exception), strng)

        d = rec.__dict__.copy()
        rec.update()
        self.assertEqual(rec.__dict__, d)

    def test_uodate2(self):
        """test update method"""
        rec = Rectangle(5, 2)
        d = rec.__dict__.copy()

        rec.update(10)
        d["id"] = 10
        self.assertEqual(rec.__dict__, d)

        rec.update(10, 5)
        d["_Rectangle__width"] = 5
        self.assertEqual(rec.__dict__, d)

        rec.update(10, 5, 17)
        d["_Rectangle__height"] = 17
        self.assertEqual(rec.__dict__, d)

        rec.update(10, 5, 17, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rec.__dict__, d)

        rec.update(10, 5, 17, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rec.__dict__, d)

    def test_update3(self):
        """test update method"""
        rec = Rectangle(5, 2)
        d = rec.__dict__.copy()

        rec.update(10)
        d["id"] = 10
        self.assertEqual(rec.__dict__, d)

        with self.assertRaises(ValueError) as exc:
            rec.update(10, -5)
        strng = "width must be > 0"
        self.assertEqual(str(exc.exception), strng)

        with self.assertRaises(ValueError) as exc:
            rec.update(10, 5, -17)
        strng = "height must be > 0"
        self.assertEqual(str(exc.exception), strng)

        with self.assertRaises(ValueError) as exc:
            rec.update(10, 5, 17, -20)
        strng = "x must be >= 0"
        self.assertEqual(str(exc.exception), strng)

        with self.assertRaises(ValueError) as exc:
            rec.update(10, 5, 17, 20, -25)
        strng = "y must be >= 0"
        self.assertEqual(str(exc.exception), strng)

    def test_update3(self):
        """test update method"""
        rec = Rectangle(5, 2)
        d = rec.__dict__.copy()

        rec.update(id=10)
        d["id"] = 10
        self.assertEqual(rec.__dict__, d)

        rec.update(width=5)
        d["_Rectangle__width"] = 5
        self.assertEqual(rec.__dict__, d)

        rec.update(height=17)
        d["_Rectangle__height"] = 17
        self.assertEqual(rec.__dict__, d)

        rec.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rec.__dict__, d)

        rec.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rec.__dict__, d)

    def test_update5(self):
        """test update method"""
        rec = Rectangle(5, 2)
        d = rec.__dict__.copy()

        rec.update(id=10)
        d["id"] = 10
        self.assertEqual(rec.__dict__, d)

        rec.update(id=10, width=5)
        d["_Rectangle__width"] = 5
        self.assertEqual(rec.__dict__, d)

        rec.update(id=10, width=5, height=17)
        d["_Rectangle__height"] = 17
        self.assertEqual(rec.__dict__, d)

        rec.update(id=10, width=5, height=17, x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rec.__dict__, d)

        rec.update(id=10, width=5, height=17, x=20, y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rec.__dict__, d)

        rec.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(rec.__dict__, d)

        Base._Base__nb_objects = 0
        rec1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rec1), "[Rectangle] (1) 10/10 - 10/10")

        rec1.update(height=1)
        self.assertEqual(str(rec1), "[Rectangle] (1) 10/10 - 10/1")

        rec1.update(width=1, x=2)
        self.assertEqual(str(rec1), "[Rectangle] (1) 2/10 - 1/1")

        rec1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rec1), "[Rectangle] (89) 3/1 - 2/1")

        rec1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rec1), "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        rec1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rec1), "[Rectangle] (1) 10/10 - 10/10")

        rec1.update(89)
        self.assertEqual(str(rec1), "[Rectangle] (89) 10/10 - 10/10")

        rec1.update(89, 2)
        self.assertEqual(str(rec1), "[Rectangle] (89) 10/10 - 2/10")

        rec1.update(89, 2, 3)
        self.assertEqual(str(rec1), "[Rectangle] (89) 10/10 - 2/3")

        rec1.update(89, 2, 3, 4)
        self.assertEqual(str(rec1), "[Rectangle] (89) 4/10 - 2/3")

        rec1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rec1), "[Rectangle] (89) 4/5 - 2/3")

    def test_dict(self):
        """test dictionary"""
        with self.assertRaises(TypeError) as exc:
            Rectangle.to_dictionary()
        strng = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(exc.exception), strng)

        rec = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(rec.to_dictionary(), d)

        rec = Rectangle(1, 2, 3, 4, 5)
        d = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(rec.to_dictionary(), d)

        rec.x = 10
        rec.y = 20
        rec.width = 30
        rec.height = 40
        d = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(rec.to_dictionary(), d)

        rec1 = Rectangle(10, 2, 1, 9)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle(1, 1)
        rec2.update(**rec1_dictionary)
        self.assertEqual(str(rec1), str(rec2))
        self.assertNotEqual(rec1, rec2)

if __name__ == "__main__":
    unittest.main()
