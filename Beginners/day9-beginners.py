def fibSum(n):
    '''

    '''
    if type(n) != int:
        return ("invalid input, number must be a positive integer")
    if n < 0:
        return ("Invalid, number can't be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        a = 0
        b = 1
        m = []
        for i in range(2,n):
            c = a + b
            a,b = b,c
            m.append(c)
        res = sum([i for i in m if i <= n and i % 2 == 0])
    return res

print(fibSum(1000))

        
