data=input()
arr=[]
for i in range(len(data)):
    arr.append(int(data[i]))
result=arr[0]

for i in range(len(data)-1):
    if arr[i]==0 or arr[i]==1:
        result+=arr[i+1]
    else:
        result*=arr[i+1]
print(result)
