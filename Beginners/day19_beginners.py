def variableParam(*args):
    '''

    '''
    def bin2dec(n):
        return int(n,2)
    t = []
    for i in args:
        if bin2dec(i) % 5 == 0:
            t.append(i)
    return tuple(t)

print(variableParam('0100','0011','-1010','1001'))
            
print(variableParam('0100','0011'))
