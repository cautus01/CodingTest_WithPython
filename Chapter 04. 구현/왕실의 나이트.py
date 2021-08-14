# 좌표 입력받기
s=input()
x=ord(s[0])-ord('a')+1
y=int(s[1])
# 나이트가 이동할 수 있는 8가지 방향 정의
direction=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

count=0
for dir in direction:
    nx=x+dir[0]
    ny=y+dir[1]
    # 만약 해당 위치라면 무시
    if nx<1 or nx>8 or ny<1 or ny>8:
        continue
    count+=1
# 결과 출력
print(count)
