def fastSum(n):
	'''
	The function takes in a number and returns the sum of its first n terms.
	
	'''
	assert type(n)==int, 'Only integers are allowed'
	
	#This is a test of time complexity and this code gave me the best result.
	
	return (n+n**2)//2

