#!/usr/bin/python3
""" Square class """


class Square:
    """ empty class Square that defines a square

    Attributes:
        size: size of the square
    """
    __size = 0

    def __init__(self, prmSize=0):
        self.size = prmSize

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, prmSize=0):
        if not isinstance(prmSize, int):
            raise TypeError("size must be an integer")
        elif prmSize < 0:
            raise ValueError("size must be >= 0")
        self.__size = prmSize

     def my_print(self):
         for y in range(self.size):
             [print("#", end='') for x in range(self.size)]
             print()
         if self.size == 0:
             print()
