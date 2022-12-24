import math

class Circle:
    def __init__(self, radius=3):
        self.__radius = radius

    def getPerimeter(self):
        return 2 * math.pi * self.__radius

    def getArea(self):
        return math.pi * self.__radius * self.__radius

    def setRadius(self, radius):
        self.__radius = radius
