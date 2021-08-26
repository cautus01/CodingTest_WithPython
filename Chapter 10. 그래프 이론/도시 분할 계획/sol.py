def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 마을의 개수와 길의 개수 입력
n,m=map(int,input().split())
edges=[] # 간선 정보 저장
parent=[0]*(n+1) # 부모 테이블

# 부모를 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i]=i
# 간선 정보 입력
for _ in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
edges.sort() # 정렬

result=0
max_value=0
for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        max_value=cost
print(result-max_value)
