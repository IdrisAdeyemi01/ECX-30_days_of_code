def even_odd(list_num):
    '''
    Parameter: list_num( a list of integers)
    Output: A print statement showing number of even and odd integers in the list    
    '''
    if not type(list_num) is list:
        if not type(list_num) is range:
            raise TypeError('The only required type for list_num is list')
    elif type(list_num) == list or range:
        for i in list_num:
            if type(i) != int:
                raise ValueError('The list can only contain integers')
    even_count= 0
    odd_count= 0
    for i in list_num:
        if i%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print('number of even numbers is,',even_count)
    print('number of odd numbers is,', odd_count)

even_odd([1,2,3,4,5,6,7,8,9,10,18])
even_odd(range(10,35))
        
