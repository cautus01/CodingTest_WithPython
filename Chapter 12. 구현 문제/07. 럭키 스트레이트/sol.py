data=input()
n=len(data)//2
n1,n2=0,0

for i in range(n):
    n1+=int(data[i])
for i in range(n,len(data)):
    n2+=int(data[i])

if n1==n2:
    print("LUCKY")
else:
    print("READY")
