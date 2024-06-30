## Problem1 (https://leetcode.com/problems/coin-change/)

class Solution:
    def coinChange(self, coins, amount):
        # Initialize the dp array with amount + 1, which represents an unreachable amount
        dp = [amount+1] * (amount + 1)
        # Base case: to make 0 amount, we need 0 coins
        dp[0] = 0
        for amt in range(1, amount+1):
            for coin in coins:
                # If the coin can be used (i.e., it is not larger than the current amount)
                if amt - coin >= 0:
                    # Update dp[amt] with the minimum number of coins needed
                    dp[amt] = min(dp[amt], 1+ dp[amt-coin])
        
        # If dp[amount] is still amount + 1, 
        if dp[amount] == amount + 1:
            return -1 #it means the amount cannot be reached with the given coins 
        else:
            return dp[amount]


sol = Solution()
coins = [1,2,5]
amount = 11
print(sol.coinChange(coins,amount))