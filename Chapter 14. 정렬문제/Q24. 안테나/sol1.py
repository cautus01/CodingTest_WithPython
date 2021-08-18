# n 입력
n=int(input())
# 집의 위치 입력
data=list(map(int,input().split()))
data.sort()

min_value=int(1e9)
min_index=0
for x in data:
    result=0
    for i in data:
        result+=abs(x-i)
    if min_value>result:
        min_value=result
        min_index=x
print(min_index)
