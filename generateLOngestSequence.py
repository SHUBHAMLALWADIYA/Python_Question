# def solve(i,j,s1,s2):
    
#     if i<0 or j<0:
#         return 0
#     if (s1[i]==s2[j]):
#         return 1+solve(i-1,j-1,s1,s2)
#     takeS1=solve(i-1,j,s1,s2)   
#     takeS2=solve(i,j-1,s1,s2)
    
#     return max(takeS1,takeS2)


#dp approch
def solve(i,j,s1,s2,dp):
    
    if i==0 or j==0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if (s1[i-1]==s2[j-1]):
        dp[i][j]=1+solve(i-1,j-1,s1,s2,dp)
        return dp[i][j]
    takeS1=solve(i-1,j,s1,s2,dp)   
    takeS2=solve(i,j-1,s1,s2,dp)
    
    dp[i][j]=max(takeS1,takeS2)
    return dp[i][j]

    
def main():
    s1="abc"
    s2="abc"
    i=len(s1)-1
    j =len(s2)-1
    dp = [[-1 for _ in range(j+1)] for _ in range(i+1)]
    print(solve(i,j,s1,s2,dp))
main()


