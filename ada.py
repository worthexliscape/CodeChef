a=int(raw_input())
for i in range(0,a):
	b = raw_input().strip()
	
	countU=0
	countD=0
	counter=0
	c=0
	blen=len(b)

	
	for j in range(0,blen):
		if (b[j] == 'U'):
			countU+=1
		else:
			countD+=1
	
	if (blen != countU or blen != countD):
		
		if (countU>=countD):
			for k in range(0, blen):

				if (b[k]=="D"):
					if (counter==0):
						counter=1
						c+=1
				else:
					counter=0

			print c
		else:
			for k in range(0, blen):
				if (b[k]=="U"):
					if (counter==0):
						counter=1
						c+=1
					else:
						counter=0
				else:
					counter=0
			print c