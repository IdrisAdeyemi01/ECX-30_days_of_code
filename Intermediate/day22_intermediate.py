class Node():

    def __init__(self, value, left = None, right = None):

        assert type(value) == int, 'The value should be an integer'
        self.value = value
        self.left = left
        self.right = right

def insert_to_tree(arr):
    '''

    '''
    assert type(arr) == list, 'the function only takes in arrays'
    rt = Node(arr[0])
    arr = arr[1::]
    
    n= 1
    for i in arr:
        n += 1
        if i < rt.value:
            if rt.left == None:
                rt.left = Node(i)
            else:
                if i < rt.left.value:
                    rt.left = insert_to_tree(arr[arr.index(i)::])
                
                
        else:
            if rt.right == None:
                rt.right = Node(i)
            else:
                insert_to_tree(arr[arr.index(i)::])

    return rt

root = insert_to_tree([5,3,7,8,2,4,11,12,10,-4])
print(root.left.left.value)
          
