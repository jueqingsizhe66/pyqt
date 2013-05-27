
#date :2013-1-16
#author :zhaoliang
#function: factorial
def factorial(n):
	if n < 2:
		return 1
	f = 1
	while n >= 2:
		f *= n
		n -= 1
	return f
