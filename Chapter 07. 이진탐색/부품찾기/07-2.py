# n과 부품번호 입력
n=int(input())
n_arr=list(map(int,input().split()))
n_arr.sort()
# m과 부품번호 입력
m=int(input())
m_arr=list(map(int,input().split()))

def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if arr[mid]==target:
        return True
    elif arr[mid]>target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)

# m_arr의 부품이 있는지 확인
for i in m_arr:
    if binary_search(n_arr,i,0,len(n_arr)-1)==None:
        print("no",end=' ')
    else:
        print("yes",end=' ')
