class Shape:

    def __init__(self, length):
        assert type(length) == int or type(length) == float, 'The length should be a number'
        assert length >= 0, 'Length should be greater than 0'
        self.length = length
        #self.area = 0
        
    def shape(self):
        '''
        This function simply returns a string: I am a shape
        '''
        return 'I am a shape.'
    def area(self):
        return 0

    
    
class Square:

    def __init__(self,length):
        assert type(length) == int or type(length) == float, 'The length should be a number'
        assert length >= 0, 'Length should be greater than 0'
        Shape.__init__(self,length)
        self.length = length
        #self.area = self.length ** 2

    def area(self):
        '''
        This function returns the area of the square
        '''
        return self.length**2
    
