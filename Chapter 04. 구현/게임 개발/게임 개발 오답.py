# n,m 입력받기
n,m=map(int,input().split())
# x,y,dir 입력
x,y,dir=map(int,input().split())
# 2차원 리스트 입력받기
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
# 방문여부
visited=[[0]*m for _ in range(n)]
count=0 # 방문한 칸 수
rotation=0
# x와 y 이동 리스트
dx=[-1,0,1,0]
dy=[0,1,0,-1]
x,y=0,0
while True:
    while rotation<4:
        # 현재 방향을 기준으로 왼쪽 방향
        if dir==0:
            dir=3
        dir-=1
        
        nx=x+dx[dir]
        ny=y+dy[dir]
        
        if nx<0 or ny<0 or nx>=n or ny>=n:
            rotation+=1
            continue
        if visited[nx][ny]==0 and arr[nx][ny]==0:
            x=nx
            y=ny
            count+=1
            rotation=0
        else:
            rotation+=1
    if  arr[x-dx[dir]][y-dy[dir]]==0:
        break
print(count)
