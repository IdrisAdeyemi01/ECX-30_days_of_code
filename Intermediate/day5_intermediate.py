def wedding_chow(chow):
    '''
    This fuction takes in a string representing supplies(as encoded by the problem statement and its known as chow.
    It outputs a tuple that consist of two element.
    1. an integer showing the max number of complete supplies
    2. a string showing leftovers in an order specified in the problem statement (i.e rsmfd)
    N.B: only lower cases of r,s,m,f and d are considered relevant in the string provided
    '''
    if not type(chow) is str:
        raise TypeError('Only string inputs can be processed')
    r = []
    s = []
    m = []
    f = []
    d = []
    for i in chow:
        if i == 'r':
            r.append(i)
        elif i == 's':
            s.append(i)
        elif i == 'm':
            m.append(i)
        elif i == 'f':
            f.append(i)
        elif i == 'd':
            d.append(i)
    lol = [r,s,m,f,d]
    num = min([len(i) for i in lol])
    p = num
    while p>0:
        for j in lol:
            j.pop(p-1)
        p -= 1
               
    remainder = []
    for i in lol:
        #for k in range(len(lol)):
        remainder += i
    leftover = ''.join(remainder)
    return num, leftover

# Sample
print(wedding_chow('fdrsmssrrdr'))
