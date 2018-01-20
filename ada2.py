for i in range(input()):
    a=raw_input()
    n=len(a)
    c=1
    x=a[0]
    for i in range(1,n):
        if a[i]!=x:
            c+=1 
        x=a[i]
    print c/2