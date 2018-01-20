T=int(raw_input())
for i in range(0,T):
	s=map(int,raw_input().strip().split())
	slen=len(s)
	s1=map(int,raw_input().strip().split())
	x=set(s1)
	s2=map(int,raw_input().strip().split())
	y=set(s2)
	print len(x&y)