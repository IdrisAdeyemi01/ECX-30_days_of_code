def make_car(a, b, **others):
    '''
    This function takes in two compulsory strings and other parameters and returns
    a dictionary containing the first two parameters in form of manufacturer and model and other values too in a dictionary
    
    '''
    d= {'manufacturer': a, 'model' : b}
    num = 0
    for i in others:
         d[i] = others[i]
         num += 1
         if num == 2:
             break

    return d
         
        
