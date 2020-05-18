def bubble_sort(num_list):
    '''
    This function takes in a list and returns the sorted form of the list'
    '''
    assert type(num_list) == list, 'The function should contain a list'
    for i in num_list:
        assert type(i) == int, 'The list should only contain integers' 
    swap = True

    while swap:
        swap = False
        for j in range(len(num_list)-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swap = True
    return num_list
