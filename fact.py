def fibo(n):
	a=1
	for i in range(1,n+1):
		a=a*i
	return a

a=int(raw_input())
for i in range(0,a):
	b=int(raw_input())
	print fibo(b)

