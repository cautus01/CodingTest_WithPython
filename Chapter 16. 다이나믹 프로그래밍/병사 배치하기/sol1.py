n=int(input())
data=list(map(int,input().split()))

data.reverse()

d=[0]*n
d[0]=1

for i in range(1,n):
    max_value=0
    for j in range(i):
        if data[i]>data[j]:
            max_value=max(max_value,d[j])
    if max_value==0:
        d[i]=d[i-1]
    d[i]=max_value+1
    
print(n-max(d))
