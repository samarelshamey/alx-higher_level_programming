#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''
    def setUp(self):
        """setupt"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """clean after test"""
        pass

    def test_attribute(self):
        """test nb_objects"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_construct(self):
        """test construct"""
        with self.assertRaises(TypeError) as ex:
            Base.__init__()
        message = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ex.exception), message)

    def test_construct2(self):
        """test construct arg"""
        with self.assertRaises(TypeError) as ex:
            Base.__init__(self, 1, 2)
        message = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(ex.exception), message)

    def test_initialization(self):
        """test if nb_objects is zero"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        """test instantiation"""
        base = Base()
        self.assertEqual(str(type(base)), "<class 'models.base.Base'>")
        self.assertEqual(base.__dict__, {"id": 1})
        self.assertEqual(base.id, 1)

    def test_id(self):
        """test id"""
        base = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), base.id)

    def test_id2(self):
        """test id"""
        base = Base()
        base = Base("Foo")
        base = Base(98)
        base = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), base.id)

    def test_id3(self):
        """test id"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_id4(self):
        """test id"""
        i = 8
        base = Base(i)
        self.assertEqual(base.id, i)

    def test_id5(self):
        """test id"""
        i = "id"
        base = Base(i)
        self.assertEqual(base.id, i)

    def test_id6(self):
        """test id"""
        i = 654
        base = Base(id=i)
        self.assertEqual(base.id, i)

    def test_to_json(self):
        """test to json method"""
        with self.assertRaises(TypeError) as ex:
            Base.to_json_string()
        strng = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(ex.exception), strng)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        ar = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(ar)),
                         len(str(ar)))

        ar = [{'x': 115, 'y': 2063, 'width': 3512321, 'id': 1522244,
             'height': 343402}]
        self.assertEqual(len(Base.to_json_string(ar)),
                         len(str(ar)))

        ar = [{"wordooo": 787878}]
        self.assertEqual(Base.to_json_string(ar),
                         '[{"wordooo": 787878}]')

        ar = [{"wordooo": 787878}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(ar),
                         '[{"wordooo": 787878}, {"abc": 123}, {"HI": 0}]')

        ar = [{}]
        self.assertEqual(Base.to_json_string(ar),
                         '[{}]')

        ar = [{}, {}]
        self.assertEqual(Base.to_json_string(ar),
                         '[{}, {}]')

        rec = Rectangle(10, 7, 2, 8)
        dictionary = rec.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        rec1 = Rectangle(11, 9, 3, 6)
        rec2 = Rectangle(6, 1, 3, 5)
        rec3 = Rectangle(4, 3, 6, 7)
        dictionary = [rec1.to_dictionary(), rec2.to_dictionary(),
                      rec3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        rec1 = Square(11, 6, 4)
        dictionary = rec1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(11, 6, 4)
        r2 = Square(2, 5, 9)
        r3 = Square(3, 4, 6)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    def test_save_to_file(self):
        """test save to file method"""
        import os
        rec1 = Rectangle(9, 10, 2, 8)
        rec2 = Rectangle(2, 4)
        Rectangle.save_to_file([rec1, rec2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        rec2 = Rectangle(2, 4)
        Rectangle.save_to_file([rec2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        rec2 = Square(1)
        Square.save_to_file([rec2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    def test_from_json(self):
        """test from json method"""
        with self.assertRaises(TypeError) as exc:
            Base.from_json_string()
        strng = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(exc.exception), strng)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        strng1 = [{}, {}]
        strng2 = '[{}, {}]'
        self.assertEqual(Base.from_json_string(strng2), strng1)

        strng1 = [{}]
        strng2 = '[{}]'
        self.assertEqual(Base.from_json_string(strng2), strng1)

        strng1 = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 123, "y": 25623, "width": 782321, "id": 562244, "height": 89340}]'
        strng2 = [{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 123, "y": 25623, "width": 782321, "id": 562244, "height": 89340}]
        self.assertEqual(Base.from_json_string(strng1), strng2)

        strng1 = [{"wordooo": 9797978}, {"abc": 123}, {"HI": 0}]
        strng2 = '[{"wordooo": 9797978}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(strng2), strng1)

        strng1 = [{"wordooo": 9797978}]
        strng2 = '[{"wordooo": 9797978}]'
        self.assertEqual(Base.from_json_string(strng2), strng1)

        strng1 = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        strng2 = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(strng2), strng1)

        strng1 = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
                  'height': 34340}]
        strng2 = '[{"x": 101, "y": 20123, "width": 312321, "id": 522244, \
"height": 34340}]'
        self.assertEqual(Base.from_json_string(strng2), strng1)

        list1 = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list2 = Rectangle.from_json_string(
            Rectangle.to_json_string(list1))
        self.assertEqual(list1, list2)

    def test_create(self):
        """test create method"""
        rec1 = Rectangle(4, 9, 3)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual(str(rec1), str(rec2))
        self.assertFalse(rec1 is rec2)
        self.assertFalse(rec1 == rec2)

    def test_load_from_file(self):
        """test load from file method"""
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(2, 4)
        list1 = [rec1, rec2]
        Rectangle.save_to_file(list1)
        list2 = Rectangle.load_from_file()
        self.assertNotEqual(id(list1[0]), id(list2[0]))
        self.assertEqual(str(list1[0]), str(list2[0]))
        self.assertNotEqual(id(list1[1]), id(list2[1]))
        self.assertEqual(str(list1[1]), str(list2[1]))

        s1 = Square(7)
        s2 = Square(9, 3, 2)
        list1 = [s1, s2]
        Square.save_to_file(list1)
        list2 = Square.load_from_file()
        self.assertNotEqual(id(list1[0]), id(list2[0]))
        self.assertEqual(str(list1[0]), str(list2[0]))
        self.assertNotEqual(id(list1[1]), id(list2[1]))
        self.assertEqual(str(list1[1]), str(list2[1]))

    if __name__ == "__main__":
        unittest.main()
