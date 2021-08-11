# 노드, 간선의 개수 입력
n,m=map(int,input().split())

# 부모 테이블 초기화
parent=[0]*(n+1)

# 각 노드의 부모를 자기 자신으로 만들기
for i in range(1,n+1):
    parent[i]=i
    
# union 연산 각각 수행
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def parent_union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b
        
for i in range(m):
    a,b=map(int,input().split())
    parent_union(parent,a,b)
    
# 각 원소가 속한 집합 출력
for i in range(1,n+1):
    print(find_parent(parent,i),end=' ')
    
print()

# 부모 테이블 출력
for i in range (1,n+1):
    print(parent[i], end=' ')
