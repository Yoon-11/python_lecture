import math

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def getAera(self):
        return math.pi * self.radius**2

    def setRaidus(self, radius):
        self.radius = radius
