
def gBad(n,k,s):
	if (s>=n-k):
		return 1
	else:
		return 0	
def gGood(n,k,s):
	if (s>=n-k):
		return 1
	else:
		return 0
def ans(a,b):
	if (a==0 and b==0):
		return "none"
	elif (a==1 and b==0):
		return "chef"
	elif (a==0 and b==1):
		return "brother"
	elif (a==1 and b==1):
		return "both"



number=int(raw_input())
for j in range(0,number):
	nn=0
	u=0
	a=raw_input().strip().split()
	length = int(a[0])
	err=int(a[1])
	inp=raw_input()
	n=len(inp)	

	for i in inp:
		if i.islower():
			nn=nn+1
		else:
			u=u+1
	# print n,err,nn,u
	final=gBad(n,err,nn)
	final2=gGood(n,err,u)
	
	print ans(final, final2)
