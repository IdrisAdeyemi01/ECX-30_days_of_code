def k_largest(arr,k):
	'''
	The function takes in two parameters, a list and an integer value and returns the kth largest values in the arr
	'''
	assert type(arr) == list and type(k) == int, "The arr should be a list and k an integer"
	for i in arr:
		assert type(i) == int
	
		
	for j in range(len(arr)):
		for m in range(j+1, len(arr)):
			
			if arr[j] > arr[m]:
				arr[j], arr[m] = arr[m], arr[j]
		
	return arr[-k]
	
print(k_largest([7, 4, 6, 3, 9, 1],2))
		