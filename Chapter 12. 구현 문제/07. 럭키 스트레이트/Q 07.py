n=input()
arr=[]
a,b=0,0
for i in range(len(n)):
    arr.append(int(n[i]))
for i in range(0,len(n)//2):
    a+=arr[i]
for i in range(len(n)//2,len(n)):
    b+=arr[i]
if a==b:
    print("LUCKY")
else:
    print("READY")
