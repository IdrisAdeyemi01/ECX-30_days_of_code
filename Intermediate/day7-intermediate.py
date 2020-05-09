def my_car(l):
    '''
    The function takes in a list(worth of cars) and returns the maximum worth that can be obtained.
    '''
    assert type(l) == list, 'Onlist a list is allowed as input'
    for i in l:
        assert type(i) == int, 'List can only contain integers'
        assert i >= 1, 'The values must be greater than 1'

    if l[1] > l[0]:
        l.pop(0)
    print(l)

    new_l = 0
    w = len(l)
    for i in range(w):
        if i % 2 == 0:
            #if l[i+1] == l[i+2]:
            #    l.pop(i+1)
            #    w -= 1
            
            if l[i+1] == l[-1]:
                new_l += l[i]
                break
            elif l[i+2] == l[-1] or l[i+1] == l[i+2] or l[i+1]+l[i+2]<l[i+3]:
                new_l += l[i]
                l.pop(i+1)
                
                new_l += l[i+2]
                break
            
            new_l += l[i]
        
    return new_l

print(my_car([16,1,7,5,14,3,13,17,9,8,11,14,10]))

