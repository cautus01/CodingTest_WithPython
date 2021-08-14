# 정수 n 입력받기
n=int(input())
count=0

# 3이 하나라도 들어있는 시각의 수 구하기
for i in range(0,n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
# 결과값 출력            
print(count)
