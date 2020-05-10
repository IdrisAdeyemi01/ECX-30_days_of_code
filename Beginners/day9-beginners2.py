def fibSum(num):
    '''
    The function takes in a number and returns the sum of even terms in the sequence between 1 and the number(inclusive).

    Parameter:
    An integer which is the number we are checking on

    Output:
    The sum of fibonacci sequence which are even from 1 to num
    '''
    if type(num) != int:
        return ("Invalid input, number must be positive integer")
    elif num < 0:
        return ("Invalid, number can't be negative")
    elif num == 0:
        return 0
    elif num == 1:
        return 0
    n = num
    store = {}
    def fib(n):
        if n in store:
            return store[n]
        if n == 1:
            res = 1
        elif n == 2:
            res = 1
        elif n > 2:
            res = fib(n-1) + fib(n-2)
        store[n] = res
        return res
    m = []
    for i in range(2,num+2):
        m.append(fib(i))
    print(m)
    final = sum([j for j in m if j <= num and j % 2 == 0])
    return final

print(fibSum(10))       
