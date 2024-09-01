import math
import unittest


class Circle:

    def __init__(self, radius):
        self.mRadius = radius
        return

    def getRadius(self):
        return self.mRadius

    def setRadius(self, radius):
        if radius >= 0.0:
            self.mRadius = radius
            return True
        else:
            return False

    def getArea(self):
        return math.pi * self.mRadius * self.mRadius

    def getCircumference(self):
        return 2. * math.pi * self.mRadius