def squareSum(n):
    '''
    The function takes in a number, n, and returns the difference between the sum of the squares of the first nth ntural numbers and the square of the sum.
    
    '''
    if type(n) != int:
        return 'Invalid'
    if n < 1:
        return 'Wrong Input'
    square_add = 0
    normal_add = 0
    for i in range(1,n+1):
        square_add += i**2
        normal_add += i
    normal_addsq = normal_add**2
    
    return normal_addsq - square_add


        
        
