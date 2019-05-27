class A:
    def __init__(self,x):
        self.x = x
    def __repr__(self):
        return '{}'.format(self.x)
    def __add__(self, other):
        print('add')
        return self.x + other
    def __radd__(self, other):
        print('radd')
        return self.x + other
a1 = A(4)
print(a1 + 1)
print(1 + a1)
print(a1 + A(10))
class B:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        if t
