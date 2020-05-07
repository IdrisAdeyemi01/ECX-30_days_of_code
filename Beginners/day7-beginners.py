def averageMultiple(num):
    '''
    The function takes in a number and returns the average of the sum of multiples of 3 and 5.

    Parameters:
    num: The number we are considering which must be between 1 and 5000

    Output:
    Returns the average of the sum of all multiples of 3 or 5
    '''
    assert type(num) == int, 'Only integers are allowed as input'
    assert 1 < num < 5000, 'Number must be between 1 and 5000'
    
    if num <= 3:
        return 0
    
    multi_list = []
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            multi_list.append(i)
    average = sum(multi_list)/ len(multi_list)
    return average

