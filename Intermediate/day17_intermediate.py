def combo(lis, num):
    '''

    '''
    new_l = []

    j = 1
    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)):
            new_l.append([lis[i]] + lis[j:num])
            
        
        

    return new_l

print(combo([1,2,3],2))
print(combo([1,2,3,4,5],4))

