class Point:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({},{})'.format(self.x, self.y)

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
    
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Point(new_x, new_y)

    def __mul__(self, other):
        assert type(other) != str, ' The __mul__ cannot take in string'
        if type(other) == int or type(other) == float:
            m = self.x * other
            n = self.y * other
            return Point(m,n)
        else:
            m = self.x * other.x
            n = self.y * other.y
            return m + n

    def distance(self, other):
        x = (self.x - other.x)**2
        y = (self.y - other.y)**2
        return (x + y)**0.5
