for _ in range(int(raw_input())):
	b=map(int,str(raw_input().strip()))
	
	blen=len(b)
	d=list(set(b))
	
	c=0
	if (len(d)==1):
		print "uniform"
	else:
		temp=b[0]
		for i in range(1,blen):
			if (temp!=b[i]):
				c+=1
				if (c==3):
					print "non-uniform"
					break
				else:
					temp=b[i]
			

		if (c<=2):
			if (b[0]==b[blen-1]):
				print "uniform"
			else:
				c+=1
				if(c>=3):
					print "non-uniform"
				else:
					print "uniform"