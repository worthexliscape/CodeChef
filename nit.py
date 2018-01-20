a=int(raw_input())
for i in range(0,a):
	b=raw_input().strip().lower().title().split()
	if (len(b)==1):
		print b[0]
	else:	
		print ". ".join([x[0] for x in b[0:-1]])+str(". ")+b[-1]

	
	
		