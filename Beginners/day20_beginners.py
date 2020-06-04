def create_arr(X,Y):
    '''
    The function takes in 2 digits and returns a 2d array
    '''
    assert type(X) == int and type(Y) == int, 'The function only takes in integers'
    assert X >= 0 and Y >= 0, 'The values should not be negative'
    li = []
    for i in range(X):
        li2 = []
        for j in range(Y):
            li2.append(i*j)
        li.append(li2)
        

    return li

