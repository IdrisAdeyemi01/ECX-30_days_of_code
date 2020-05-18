def adder(arr):
    '''
    This function takes in a list of stringed fraction and returns their addition in stringed form to the lowest term.
    
    '''
    assert type(arr) == list, 'The parameter should be an array'
    for i in arr:
        assert type(i) == str, 'The list only contain integers'
    a = []
    for i in arr:
        a.append(i.split('/'))
    
    
    m = []
    lcm = 1
    #while lcm >= 1:
    for j in a:
        m.append(j[1])
    m = [int(i) for i in m]
    m.sort()
    mul = 1
    for i in m:
        mul *= i
    for j in range(max(m),mul+max(m),max(m)):
        if j % m[0] == 0 and j % m[1] == 0:
            lcm = j
            break
    print(lcm)
    n = []
    for k in m:
        num = lcm/int(k)
        n.append(num)
    
    print(n)
    p = []
    for i in range(len(a)):
        p.append(n[i]*int(a[i][0]))
    print(p)
    if lcm == int(sum(p)):
        return '1/1'
    
    if lcm % sum(p)!= 0:
        return str(int(sum(p))) + '/'  + str(lcm)
    else:
        for i in range(lcm-1,1,-1):
            if lcm % i == 0 and sum(p) % i == 0:
                z = i
                break
            
        return '/'.join([str(int(sum(p)/z)),str(int(lcm/z))])

print(adder(['2/21','1/9','8/63']))
print('\n')
print(adder(['1/2','1/3','1/6']))

def swapper(a,b):
    '''
    This function takes in two params and then swaps them.
    '''
    h = []
    for i in a,b:
        h.append()
    return h[1],h[0]
