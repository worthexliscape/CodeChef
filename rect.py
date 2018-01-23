for _ in range(int(raw_input())):
	b=map(int,raw_input().strip().split())
	d=list(set(b))

	if (len(d)>2):
		print "NO"
	elif (len(d)==1):
		print "YES"
	else:
	
		if (b.count(d[0])==3 or b.count(d[1])==3):
			print "NO"
		else:
			print "YES"
