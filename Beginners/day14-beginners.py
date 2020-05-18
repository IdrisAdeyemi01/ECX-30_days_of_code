def Triangle_no(num):
    '''
    This functions takes in a number and checks if the number is a triangle number and then returns True if it is or False if it is not.
    
    '''
    assert type(num) == int, "Number can only be an integer"
    assert num > 0, "Number can neither be negative nor zero"
    li = [i for i in range(1,num+1)]
    li2= []
    n = 1
    while li:
        li2.append(li[0:n])
        li = li[n::]
        n += 1
    return len(li2[-2]) == len(li2[-1])-1
