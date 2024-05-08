# def generate(idx,arr,ans):
#     if len(ans)>0:
#         print(ans)
#     if idx==len(arr):
#         return
#     for i in range(idx,len(arr)):
#         ans.append(arr[i])
#         generate(i+1,arr,ans)
#         ans.pop()
        
        
# generate(0,"abc",[])

def generate(idx,arr,ans):
    
    if idx==len(arr):
        return ans 
    ans.append(arr[idx])
    generate(idx+1,arr,ans)
    ans.pop()
    generate(idx+1,arr,ans)
    print(ans)
generate(0,"abcd",[])