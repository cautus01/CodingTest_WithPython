# n,m,k 입력
n,m,k=map(int,input().split())
# n개의 자연수 입력
arr=list(map(int,input().split()))
# 정렬
arr.sort(reverse=True)
# 몫과 나머지 구하기
first=m//(k+1)
second=m%(k+1)

# 큰 수의 합
sum=(arr[0]*k+arr[1])*first+arr[0]*second

print(sum) # 큰 수의 합 출력
