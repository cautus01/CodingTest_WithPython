# 노드의 개수와 간선의 개수 입력받기
n,m=map(int,input().split())
# 부모 테이블 초기화
parent=[0]*(n+1)
# 부모 테이블의 부모를 각각 노드로 초기화
for i in range(1,n+1):
    parent[i]=i
    
# cycle  
cycle=False

# find_parent
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# parent_union
def parent_union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 간선의 개수만큼 반복
for i in range(m):
    a,b=map(int,input().split())
    # 루트 노드가 같다면 break
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    # 아니면 union 연산
    else:
        parent_union(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print ("사이클 발생하지 않음")
