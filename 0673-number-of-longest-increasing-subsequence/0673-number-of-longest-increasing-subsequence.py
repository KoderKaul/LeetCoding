class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp=defaultdict(list)
        n = len(nums)

        dp[n-1]=[1,1]
        for i in range(n-2,-1,-1):
            dp[i]=[1,1]
            for j in range(i+1, n):
                if nums[i]< nums[j]:
                    if 1+dp[j][0] > dp[i][0]:
                        dp[i] = [1+dp[j][0], dp[j][1]]
                    elif 1+dp[j][0] == dp[i][0]:
                        dp[i] = [1+dp[j][0], dp[j][1]+dp[i][1]]

        maxLen = 0
        res=0
        for leng,num in dp.values():
            if leng>maxLen:
                maxLen=leng
                res=num
            elif leng==maxLen:
                res+=num
        return res