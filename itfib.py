def fib_ser(n,a,b):
	if n==0:
		return 0
	elif n==1:
		return b
	else:
		return fib_ser(n-1,b,a+b)

print fib_ser(999,0,1)		