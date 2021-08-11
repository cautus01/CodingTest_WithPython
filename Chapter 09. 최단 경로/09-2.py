INF = int(1e9) # 무한

# 노드의 개수와 간선의 개수 입력
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 그래프 초기화

# 자기 자신으로 갈 때, 0으로 초기화
for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            graph[a][b] = 0

# 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    # 양방향
    graph[b][a] = 1 # 처음에 추가하지 않아 답이 이상하게 나왔다. 꼭 추가하자!

x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과값
result = graph[1][k] + graph[k][x]
if result >= INF:
    print("-1")
else:
    print(result)
