from collections import deque

# n, m , k, start 입력받기
n,m,k,start=map(int,input().split())
# 도로 간선 정보 저장 리스트
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    
visited=[False]*(n+1)
result=[0]*(n+1)

def bfs(graph,result,start):
    queue=deque()
    queue.append(start)
    count=0
    visited[start]=True
    result[start]=count
    
    while queue:
        v=queue.popleft()
        count+=1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                result[i]=count
                
bfs(graph,result,start)

if k not in result:
    print("-1")

for i in range(n+1):
    if result[i]==k:
        print(i)
