class first_class(object):
    def __init__(self, name):
        print("Welcome")
        self.name = name

    def func(self):
        print("Hi", self.name)

class more(first_class):
    def __init__(self, name, age, color):
        super().__init__(name, age) 
        self.color = color


class point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.coord = (x, y)
    
    def move(self, x, y):
        self.x += x
        self.y += y

    def out(self):
        print((self.x, self.y))

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return point(self.x * other.x, self.y * other.y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def length(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __eq__(self, other):
        return self.x == other.x and self.y == p.y

p1 = point(10, 10)
p2 = point(20, 20)
p3 = p1 + p2
p4 = p1 - p2
p5 = p1 * p2
print(p3, p4, p5)
print(p1 == p2)
print(p1 > p2)
print(p1 < p2)