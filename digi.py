for _ in range(int(raw_input())):
	b=map(int,str(raw_input().strip()))
	temp=0
	for i in range(len(b)):
		temp=temp+b[i]
	print temp