# 삼각형의 쿠기 입력받기
n=int(input())
# 정수 삼각형 입력받기
dp=[]
for i in range(n):
    dp.append(list(map(int,input().split())))

# 최대 합 구하기
for i in range(1,n):
    for j in range(len(dp[i])):
        if j==0:
            left=0
        else:
            left=dp[i-1][j-1]
        if j==i:
            up=0
        else:
            up=dp[i-1][j]
        dp[i][j]=max(left,up)+dp[i][j]
        
print(max(dp[n-1]))
