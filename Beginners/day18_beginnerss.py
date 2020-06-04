def Bcalculator(n1,n2):
    '''
    This function takes in two parameters and return the decimal
    '''
    assert type(n1)== str and type(n2)== str, 'The function only takes in strings'
    for i in n1:
        assert i == '0' or i == '1', 'Only binary inputs are allowed'
    for i in n2:
        assert i == '0' or i == '1', 'Only binary inputs are allowed'

    for j in (n1,n2):
        return int(n1,2) + int(n2,2)
