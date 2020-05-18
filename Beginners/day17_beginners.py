def OddEven(n):
	'''
    This fnction takes in a positive integer and returns the number of times you must multiply the digits in the number until we get a single digit.
    
    '''
	assert type(n) == int, 'The number should be an integer'
	assert n >= 0, 'The number should not be negative'
	if n == 0:
		return 0
	summ = 0
	for i in str(n):
	  summ += int(i)
	if summ % 2 == 0:
	  return 'Evenish'
	else:
	  return 'Oddish'

	
print(OddEven(443))
