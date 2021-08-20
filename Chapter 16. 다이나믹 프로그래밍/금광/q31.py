t=int(input()) # 테스트 케이스 입력
for _ in range(t):
    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    d=[]
    index=0
    # dp 테이블 만들기
    for i in range(n):
        d.append(data[index:index+m])
        index+=m
    
    for j in range(1,m):
        for i in range(n):
            if i==0:
                left_up=0
            else:
                left_up=d[i-1][j-1]
                
            left=d[i][j-1]
            
            if i==n-1:
                left_down=0
            else:
                left_down=d[i+1][j-1]
            
            d[i][j]=max(left_up,left,left_down)+d[i][j]
        
    result=0
    for i in range(n):
        result=max(result,d[i][m-1])
        
    print(result)
