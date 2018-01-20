n=int(raw_input())
for i in range(0,n):
	result = int(raw_input().strip())
	a=map(int,raw_input().strip().split())
	c=1
	for j in range(0,len(a)):
		if (j==len(a)-1):
			result += (c*(c-1))/2
		elif(a[j]<=a[j+1]):
				c+=1
		else:
			result+=(c*(c-1))/2
			c=1
	print result