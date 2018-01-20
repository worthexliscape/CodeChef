

T=int(raw_input())
def chef():
	c1=0
	for i in A:
		if i.isupper():
			c1=c1+1
		else:
			continue
	if c1>K:
		return 0
	else:
		return 1
def brother():
	c2=0
	for i in A:
		if i.islower():
			c2=c2+1
		else:
			continue
	if c2>K:
		return 0
	else:
		return 1


for i in range(0,T):
	s1=map(int,raw_input().strip().split(" "))
	s=raw_input()
	N=s1[0]
	K=s1[1]
	A=list(s)
	a=0
	b=0
	a=chef()
	b=brother()
	if a==1 and b==1:
		print 'both'
	elif b==1:
		print 'brother'
	elif a==1:
		print 'chef'

	else:
		print 'none' 








