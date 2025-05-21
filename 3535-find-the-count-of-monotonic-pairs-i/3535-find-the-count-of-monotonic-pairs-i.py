class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        m, n = len(nums), max(nums)
        dp = [0]*(n+1)
        for j in range(nums[0]+1):
            dp[j] = 1

        for i in range(1, m):
            curr = [0]*(n+1)
            for s in range(nums[i]+1):
                for k in range(min(s, nums[i-1])+1):
                    if nums[i-1]-k >= nums[i]-s:
                        curr[s] += dp[k]
                    curr[s] %= (1e9+7)
            dp = curr
            
        return int(sum(dp)%(1e9+7))