class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hash__ = hash((x,y))
    # __hash__ =None
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

    def __hash__(self):
        return self.hash__

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
a = Point(1, 2)
b = Point(6, 2)
# print(a.__hash__(),b.__hash__())

t = {a, b}
print(a+b)
dict()
