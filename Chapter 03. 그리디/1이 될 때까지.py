# n,k 입력
n,k=map(int,input().split())
# 최소 횟수
count=0

# n이 1이 될 때까지 반복
while True:
    # n이 1이면
    if n==1:
        break
    # n이 k로 나누어떨어지면   
    if n%k==0:
        n=n//k
        count+=1
    # n에서 1을 뺀다.    
    else:
        n-=1
        count+=1
        
print(count)
