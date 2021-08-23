# 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시 입력
import sys
INF=int(1e9)
input=sys.stdin.readline
import heapq

n,m,c=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

# 통로에 대한 정보 입력
for i in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))
                    
def dextra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dextra(c)

print(len(distance)-distance.count(INF)-1,end=' ')

max_value=0
for i in range(n+1):
    if distance[i]<INF:
        max_value=max(max_value,distance[i])
print(max_value)
