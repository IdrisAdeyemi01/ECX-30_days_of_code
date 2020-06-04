class Person:

    def __init__(self, name, age):
        assert type(name) == str and type(age) == int, 'Name should be string and age should be an integer'
        self.name = name
        self.age = age

    def addAge(self, n):
        assert type(n) == int, 'addAge takes in an integer'
        
        return '{} will be {} in the next {} years'.format(self.name,self.age+n,n)

    def printUser(self):
        return '{} is {} years old'.format(self.name, self.age)
