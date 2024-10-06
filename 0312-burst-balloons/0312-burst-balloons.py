class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #very beautifully crafted
        #idea is we solve starting with len=1 till n-1
        # at each step we take left and right points the crafts the range
        #   then we choose one item in the range to be the last ball to burst
        #     coins = coins collected from left to item + bursting this one + bursting item till right
        #       in all of these left and right are excluded from the range
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        
        for length in range(1, n-1):
            for left in range(0, n-1-length):
                right = left + length + 1
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], 
                                          nums[left]*nums[i]*nums[right] +
                                          dp[left][i] + dp[i][right])
        
        return dp[0][n-1]
        