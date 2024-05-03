def solve(n,arr):
    
    for i in range(n):
        isSwapped=0
        for j in range(n-i-1):
            
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
                isSwapped+=1
        if isSwapped==0:
            break
    print(*arr)
    

def inp():
    n=int(input())
    arr=list(map(int,input().strip().split()))
    solve(n,arr)
inp()
