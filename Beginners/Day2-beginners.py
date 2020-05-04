def missing_numbers(num_list):
    '''
    This function takes in a list of numbers as input.
    returns: the missing numbers in the list as compared to a range of the number from its beginning to its end
    
    '''
    missing= []
    for i in range(num_list[0],num_list[-1]):
        if i not in num_list:
            missing.append(i)

    return missing

print(missing_numbers([2,3,5,7,8,25]))
