from itertools import combinations

n,m=map(int,input().split())
graph=[] # 그래프 저장
datas=[] # 그래프에서 값이 0인 좌표 저장
conti=[]
for i in range(n):
    data=list(map(int,input().split()))
    graph.append(data)
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            datas.append((i,j))
        if graph[i][j]==2:
            conti.append((i,j)) 
datas=list(combinations(datas,3))

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs(graph,x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m or graph[nx][ny]==1:
            continue
        if graph[nx][ny]==0:
            graph[nx][ny]=2
            dfs(graph,nx,ny)
        
safe=0
for data in datas:
    # 벽 만들기
    graph1=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            graph1[i][j]=graph[i][j]
            
    for i in range(3):
        graph1[data[i][0]][data[i][1]]=1
        
    for start in conti:
        sx,sy=start
        dfs(graph1,sx,sy)
    result=0
    for i in range(n):
        for j in range(m):
            if graph1[i][j]==0:
                result+=1
    safe=max(safe,result)
print(safe)
