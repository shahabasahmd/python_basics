class Circle :
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius


c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(15)
print(c1.area())
print(c1.perimeter())
print(c2.area())
print(c2.perimeter())