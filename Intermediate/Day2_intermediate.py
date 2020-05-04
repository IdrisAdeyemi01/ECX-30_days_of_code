def termino(string_of_brackets):
    '''
    Function name: termino
    parameter: brackets in a string
    output: The minimum number of brackets to be removed for an open-close bracket to be filled
    
    '''
    if type(string_of_brackets) != str:
        raise 'input must be strings of brackets'
    remove_mini= 0
    for char in string_of_brackets.split('()'):
        remove_mini+= char.count('(')+ char.count(')')
    return remove_mini

print(termino('((()))()'))
