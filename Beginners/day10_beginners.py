def fibonacci(n):
	if type(n) != int:
		return "Invalid"
	if n < 0:
		return "Wrong input"
	p = (1+ (5**0.5))/2
	sq = 5 ** 0.5
	m = []
	for i in range(n+1):
		m.append(round((p ** i)/sq))
	
	if n in m:
		return True
	else:
		return False
