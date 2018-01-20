a=int(raw_input("no. of cases "))

for j in range(0, a):
    r=raw_input("no. of rows & columns ").strip().split()
    r1=int(r[0])
    c1=int(r[1])
    
    for i in range(0, r1):
        cost=0
        print("Enter the string")
        c2=raw_input().strip().replace(""," ").split()
        c2len=len(c2)
        r=[]
        g=[]
        # for i,v in enumerate(c2):
            if v == 'R':
                if i != 0 and r:
                r.append(i)
            else:
                v.append(i)
        if(c2len!=c1):
            break
        else:
            for k in range(1, c2len-1):
                if(c2[k]=="R"):
                    if(c2[k-1]=="R" and c2[k+1]=="R"):


                        c2[k]="G"
                        cost+=5
                elif(c2[k]=="G"):
                    if(c2[k+1]=="G"):
                        c2[k]="R"
                        # cost+=3
    if(c2len!=c1):
        break
    else:
        print cost          
   
