for _ in range(int(raw_input())):
	a=map(int,raw_input().strip().split())
	d=a[0]
	e=a[1]
	b = map(int,raw_input().strip().split())
	temp=float(a[0]-(a[1]*2))
	c=float(0)
	b=sorted(b)
	blen=len(b)
	z=float(0)
	
	for i in range(e,blen-e):
		z+=b[i]
		
		
	main = float(z/temp)
	print main	
	
	