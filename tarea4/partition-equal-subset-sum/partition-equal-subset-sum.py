class Solution(object):
    def canPartition(self, nums):

        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
            
        W = total_sum // 2
        
        dp = [False] * (W + 1)
        dp[0] = True  
        
        for num in nums:
            for w in range(W, num - 1, -1):
                dp[w] = dp[w] or dp[w - num]
            
            if dp[W]:
                return True
                
        return dp[W]