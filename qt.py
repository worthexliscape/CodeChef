a=int(raw_input())

for i in range(0,a):
	b=int(raw_input())
	if(b>=2 and b<=100):
		s=map(int,raw_input().strip().split())
		if(0 in s):
			break
		else:
			count=0
		
		
			slen=len(s)
		
			if(1 in s):
				m=max(s)
				for j in range(1,m):
					if(j in s):
						if(j==m-1):
							for k in range(0, slen-1):
								if(s[k+1]-s[k]==1):
									count=0
									
								else:
									count+=1
									break
					else:
						count=0
	else:
		break		
	if(count==0):
		print "no"
	else:
		print "yes"


