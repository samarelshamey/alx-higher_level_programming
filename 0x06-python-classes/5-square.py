#!/usr/bin/python3
Square = __import__('4-square').Square


def my_print(self):
    """print a square"""
    if self.__size == 0:
        print()
    else:
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
