def order(this):
    '''
    This function takes in a list of integers and returns a tuple.

    Parameter:
    this: a list of integers

    Output:
    a tuple with two parameters
    1. the length of the longest consecutive element
    2. a sorted list of the remaining elements.
    '''
    assert type(this)== list, 'This function only takes in a list'
    for i in this:
        assert type(i) == int, 'The list should only contain integers'

    this.sort()
    sequential_list= []
    sequential_l = []
    step =1
    for i in range(0,len(this),step):
        m = this[i:]
       
        if this[i]==this[-1]:
            break
        if this[i+1]- this[i]>step:
            step = this[i+1]-this[i]
        for j in range(1, len(m)+step):
            n = m[0:j]
            
            
            if n == list(range(min(n),max(n)+step,step)):
                sequential_list.append(n)
                
    for char in sequential_list:
        if len(char) == 1:
            sequential_list.remove(char)

    for k in sequential_list:
        sequential_l.append(len(k))

    maxim = max(sequential_l)
    maximum = sequential_l.index(maxim)

    res= sequential_list[maximum]

    remains = [l for l in res+this if l not in res and i not in this]

    return maxim,remains
            
                         
                         
                         
        
    
