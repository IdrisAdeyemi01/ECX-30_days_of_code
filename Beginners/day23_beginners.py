class circle:

    def __init__(self,radius):
        assert type(radius) == int or type(radius) == float, 'radius should be numbers'
        self.radius = radius

    def computeArea(self):
        pi = 22/7
        a = pi* (self.radius**2)
        return '{}cm2'.format(int(a))

    def computeCircum(self):
        pi = 22/7
        c = 2 * pi * self.radius
        return '{}cm'.format(int(c))
        
    def __repr__(self):
        return 'Circle(%s)'%(self.radius)
    
