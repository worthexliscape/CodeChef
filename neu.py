for _ in range(int(raw_input())):
	b=map(int,raw_input().strip().split())
	for i in range(0,b[0]):
		temp=0
		s=0
		ns=0
		c=map(int,raw_input().strip().split())
		for j in range(b[1],b[2]+1):
			k=0

			if (c[k]%2==0 and j%2 == 0 and c[k+1]%2==0):
				s+=1
			elif (c[k]%2!=0 and j%2!=0 and c[k+1]%2!=0):
				s+=1
			elif (c[k]%2!=0 and j%2!=0 and c[k+1]%2==0):
				ns+=1
			elif (c[k]%2==0 and j%2==0 and c[k+1]%2!=0):
				ns+=1
		print s,ns




