def PrimeSum(num):
    '''
    Takes in an integer and returns the sum of prime numbers in it.
    '''
    if not type(num) is int:
        raise TypeError('Only integers are allowed')
    def prime(x):
        ans = []
        i = 1
        while i<= x:
            a = x % i
            if a == 0:
                ans.append(a)
            if len(ans) > 3:
                break
            i +=1
        if len(ans) == 2:
            return True
        else:
            return False
    sum_prime = 0
    a = list(range(1,num))
    for t in a:
        if prime(t) == True:
            sum_prime += t
    return sum_prime

