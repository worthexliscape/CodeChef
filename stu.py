a=int(raw_input())
for i in range(0,a):

	b=raw_input().strip().replace(""," ").split()
	blen=len(b)
	count=0
	for j in range(0,blen):
		if(b[j]=="<"):
			b[j]=">"
		elif(b[j]==">"):
			b[j]="<"
	
	for k in range(0,blen):
		if(k==blen-1):
			break
		elif(b[k]==">"):
			if(b[k+1]=="<"):
				count+=1
	print count
