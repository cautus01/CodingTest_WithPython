# n,m 입력받기
n,m=map(int,input().split())
arr=[]

# 2차원 리스트 입력받기
for i in range(n):
    a=list(map(int,input().split()))
    a.sort() # 입력받은 리스트 정렬
    arr.append(a[0]) 
    
arr.sort(reverse=True)
print(arr[0])
