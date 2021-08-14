import heapq

string=input()
q=[]
q1=[]

for i in range(len(string)):
    if ord(string[i])<ord('A'):
        heapq.heappush(q,string[i])
    else:
        heapq.heappush(q1,string[i])
    
for i in range(len(q1)):
    print(heapq.heappop(q1),end='')
for i in range(len(q)):
    print(heapq.heappop(q),end='')
