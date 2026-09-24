class Solution(object):
    def coinChange(self, coins, amount):

        dp = [amount + 1] * (amount + 1)
        
        dp[0] = 0
        
        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    dp[x] = min(dp[x], dp[x - c] + 1)
                    
        return dp[amount] if dp[amount] != amount + 1 else -1