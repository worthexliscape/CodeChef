def cstr(a,index, count):
	
	c=0
	h=0
	e=0
	f=0
	count=count
	temp=0
	alen=len(a)
	for i in range(index,alen):
		if a[i]=='C':
			c+=1
		elif(c>=1):
			if a[i]=='H':
				h+=1
		elif (c>=1 and h>=1):
			if a[i]=='E':
				e+=1
		elif(c>=1 and h>=1 and e>=1):
			if(a[i]=='F'):
				count+=1
				
				c=0
				h=0
				e=0
				temp=a[i]
				if ((i+1)!=alen):
					if temp!=a[i+1]:
						cstr(a,i+1, count)
				
	return count

a=raw_input().strip()
print cstr(a,0,0)