def to_base(num, base):
    '''
	This function takes in a tuple of integers and returns a string
	
	Parameters:
	1. num: the num decimal integer to be converted
	2. the desired base to be converted into
	
	Output:
	A string of the converted form of the integer to the desired base.
    '''
    assert type(num) == int, 'num should only be an integer'
    assert type(base) == int, 'the base should be an integer'
    assert base == 2 or base==4 or base==8 or base==16, 'The base should only be 2, 4, 8 or 16'
    if num == 0:
        return '0'
    if base == 2:
        y = 1
    elif base == 4:
        y = 2
    elif base == 8:
        y = 3
    elif base == 16:
        y = 4
    def remainder(n, d):
    	if n ==0:
    		return 0
    	elif d==0:
    		return -1
    	while n>=d:
    		n = n-d
    	if d == 16:
	    	if n == 10:
	    		n = 'a'
	    	elif n == 11:
	    		n = 'b'
	    	elif n == 12:
	    		n = 'c'
	    	elif n == 13:
	    		n = 'd'
	    	elif n == 14:
	    		n = 'e'
	    	elif n == 15:
	    		n = 'f'
    	return n
    
        
    m = to_base(num>>y, base)+ str(remainder(num, (2** y)))
    
    
    return m.lstrip('0')
