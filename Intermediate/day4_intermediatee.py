def bits_of_gray(bits_num):
    '''

    '''
    if type(bits_num) != int:
        raise TypeError('Only integers are allowed as input')
    if bits_num < 1:
        raise ValueError('The input must be at least 1')
    base= ['0', '1']
    if bits_num == 1:
        return base
    if bits_num > 1:
        i = 2**(bits_num-3)
        while i > 0:
            a= base
            b= base[::-1]
            a_new= ['0' + i for i in a]
            b_new= ['1' + j for j in b]
            base= a_new+ b_new
            i -= 1
        return base

print(bits_of_gray(7))

