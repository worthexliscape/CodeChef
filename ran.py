t = input()
v=[]
for q in range(t):
    n=input()
    a=map(int,raw_input().strip().split())
    count1=0;
    x=[]
    for i in range(n):
        j=i+1;
        while(j<=n-1):
            x.append((a[i]+a[j]));
            count1+=1;
            j+=1;
    count1= float(count1)
    ff=float(x.count(max(x)))
    v.append(ff/count1)
for r in v:
    print r