import heapq
import sys
input=sys.stdin.readline
INF = int(1e9)

# 1. 노드의 개수와 간선의 개수 입력
n, m = map(int, input().split())
start=int(input())

# 2. 간선에 대한 정보를 담을 리스트와 최단거리를 저장할 리스트 초기화
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# 3. 간선에 대한 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dextra(start):
    # 4. 큐 초기화
    q = []
    # 5. 큐에 시작 노드를 넣고, 최단거리 0으로
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 6. 큐가 비어있지 않다면 반복
    while q:
        # 7. 큐 꺼내기
        dist, now = heapq.heappop(q)
        # 8. 만약 해당 노드가 이미 처리한 노드라면 무시
        if distance[now] < dist:
            continue
        # 9. 현재 노드와 연결된 다른 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] # 조심
            # 10. 만약 현재 노드를 거친 거리가 더 짧을 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dextra(start)
# 최단 거리 출력
for i in range(1,n+1):
    if distance[i]==INF:
        print("infinity")
    else:
        print(distance[i])
