def itos(integer):
    '''
    
    '''
    if type(integer) != int:
        raise ValueError('Only integer input are allowed')
    else:
        return str(integer)

def stoi(string):
    '''

    '''
    if type(string) != str:
        raise ValueError('Only strings values are allowed')
    else:
        return int(string)


def ftos(float_value):
    '''

    '''
    if not type(float_value) is float:
        raise ValueError('You can only input float values')
    else:
        return str(float_value)

def stof(string_value):
    '''

    '''
    if not type(string_value) is str:
        raise ValueError('You are only allowed to use  strings')
    else:
        return float(string_value)

    
