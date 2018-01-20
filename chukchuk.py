a=int(raw_input())
arr=["LB", "MB", "UB","LB", "MB", "UB", "SL", "SU"]


for i in range(0,a):
	inp=int(raw_input())
	d=inp%8
	
	if(d>0 and d<4):
		
		print str(inp+3)+str(arr[d+2])
	elif(d>3 and d<7):
		
		print str(inp-3)+str(arr[d-4])
	elif(d==7):
		
		
		print str(inp+1)+str(arr[d])
	else:
		
		
		print str(inp-1)+str(arr[d-2])
	