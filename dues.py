
a=int(raw_input())
for i in range(0,a):
	p=0
	m=int(raw_input())
	
	e=raw_input().strip().replace(" ","").split("0")
	p=(len(e)-1)*1100
	for v in e[1:]:
		p+=len(v)*100


	# for k in range(0,m):
	# 	if(k==0):
	# 		if(e[k]=='0'):
	# 			p=p+1100
	# 		else:
	# 			p=0
	# 	elif(p>=1100):
	# 		if(e[k]=='1'):
	# 			p=p+100
	# 		else:
	# 			p=p+1100
	# 	else:
	# 		if(e[k]=='1'):
	# 			p+=0
	# 		else:
	# 			p=p+1100
	print p		




