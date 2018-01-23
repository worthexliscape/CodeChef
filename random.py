for _ in range(int(raw_input())):
	d=int(raw_input())
	if (d>1):
		b=sorted(map(int,raw_input().strip().split()))
		
		prob=float((d*(d-1)/2))
		setb=sorted(list(set(b)))
		
		c=1
		if(len(setb)==1):
			prob=float(1)
			
				
		elif (b[-1]!=b[-2]):
			mini = b.count(setb[-2])
			prob = float(mini)/float(prob)
		else:
			temp=b[-1]
			for i in range(d-2, -1,-1):
				if(temp==b[i]):
					c+=1
					if(b.count(temp)==2):
						c=1
						break

					
				else:
					break

			prob = float(c)/float(prob)
		
		print round(prob,6)
	else:
		break