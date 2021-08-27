n,m=map(int,input().split())
parent=[0]*n

edges=[]
result=0
max_value=0

for i in range(n):
    parent[i]=i
    
for i in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
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
edges.sort()

for edge in edges:
    cost,a,b=edge
    max_value+=cost
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(max_value-result)
