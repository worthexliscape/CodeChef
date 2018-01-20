a=int(raw_input())

for i in range(0,a):
	b=int(raw_input())
	inpu = raw_input().strip()
	s=map(int,inpu.split())
	ss=sorted(s)
	output = str(ss).replace(',','')[1:-1]
	count=0
	if inpu == output:
		print "no"
		count=0
	else:	
		if (b in ss):
			j=b
			
			for j in range(j,0,-1):
				if (j in ss):
					count = 1
				else:
					count = 0
					break		
		if (count==1):
			print "yes"
		else:
			print "no"
	# if(count==1):
	# 	k=b
		
	# 	for k in range(k-1,0,-1):
	# 		if (s[k]==k+1):
	# 			count=0
	# 			break
	# 		else:
	# 			print "yes"
	# if(count==0):
	# 	print "no"