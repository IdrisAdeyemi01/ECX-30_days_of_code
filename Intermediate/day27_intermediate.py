def match(list_str):
    '''
    This function takes a list of strings and returns a tuple...
    '''
    assert type(list_str) == list, 'Takes in a list'
    for i in list_str:
        assert type(i)== str, 'The list contains strings only'
    n = 1
    new = []
    for i in list_str:
        for j in list_str[n::]:
            m = i + j
            if m == m[::-1]:
                new.append((list_str.index(i),list_str.index(j)))
        n += 1

    return tuple(new)
