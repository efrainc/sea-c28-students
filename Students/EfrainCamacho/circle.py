#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius*2
        self._area = math.pi*radius**2
    @property
    def radius(self):
        return self._radius
    @property
    def diameter(self):
        return self._diameter
    @property
    def area(self):
        return self._area
    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._diameter = radius*2
        
    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self._radius = diameter/2

    def __str__(self):
        return "Circle with radius: %s.000000"%self._radius

    def __repr__(self):
        return "Circle(%s)"%self._radius

    def __add__(self, value):
        return Circle((self._radius + value.radius))
    def __mul__(self, value):
        return Circle(self._radius * value)
    def __cmp__(self, value):
        if self._radius == value.radius:
            return False
        else:
            return True

    def __lt__(self, value):
        if self.radius < value.radius:
            return True
        else:
            return False

    def __le__(self, value):
        if self._radius <= value.radius:
            return True
        else:
            return False

    def __gt__(self, value):
        if self._radius > value.radius:
            return True
        else:
            return False
    









