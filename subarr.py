t = int(raw_input())
a = []
for i in range(t):
    q = int(raw_input())
    y = map(int,raw_input().split())
    sum2 = 0
    for i in range(len(y)):
        for j in range(i , len(y)):
            flag = 0
            sum1 = y[i]
            for p in range(i,j+1):
                if y[p] < sum1 : 
                    flag = 1
                    break
                sum1 = y[p]
            if flag == 0 :
                sum2 += 1
 
    a.append(sum2)
 
 
for i in range(t):
    print a[i]