class Solution:
    def maxSubArray(self, a: list[int]) -> int:
        n = len(a)
    
        bestending = a[0]
        ans = a[0]
        
        for i in range(1, n):
            v1 = bestending + a[i]         
            v2 = a[i]                       
            
            bestending = max(v1, v2)      
            ans = max(ans, bestending)    
            
        return ans
      