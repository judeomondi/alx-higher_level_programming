#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Class Rectangle
    Attributes:
        __width (int): width of the Rectangle
        __height (int): height of the Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes Rectangle's width and height
        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter of __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width
        Args:
            value (int): the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height
        Args:
            value (int): the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the rectangle's area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of a rectangle
            Returns:
                Formatted string representation of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            string = ""
        else:
            string = (str(self.print_symbol) * self.__width + "\n") \
                * self.__height
        return string[:-1]

    def __repr__(self):
        """return a string representation of the rectangle
         to be able to recreate a new instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
