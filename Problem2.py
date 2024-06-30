## Problem2 (https://leetcode.com/problems/house-robber/)

class Solution:
    def rob(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            #[rob1,rob2,n,n+1]
            maxAmount = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = maxAmount

        return rob2

sol = Solution()
nums = [2,7,9,3,1]
print(sol.rob(nums))