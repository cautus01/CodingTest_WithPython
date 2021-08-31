arr=[]
data=input()
num=0

for i in range(len(data)):
    if data[i].isalpha():
        arr.append(data[i])
    else:
        num+=int(data[i])
arr.sort()
print("".join(arr)+str(num))
