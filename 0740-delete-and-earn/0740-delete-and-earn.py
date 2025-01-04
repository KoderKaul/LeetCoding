class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freqDict = [0] * (max(nums)+1)
        for n in nums:
            freqDict[n] += n
        dp = [0] * len(freqDict)
        dp[1] = freqDict[1]

        for i,n in enumerate(freqDict):
            if i <=1:
                continue
            # # print(i, n, dp)
            # if i-1 in freqDict:
            #     dp[i][1]=dp[i-1][0] + n
            #     # dp[i][0]=max(dp[i-1][0], dp[i-1][1])
            # else:
            #     dp[i][1]=max(dp[i-1][0], dp[i-1][1]) + n
            # dp[i][0]=max(dp[i-1][0], dp[i-1][1])

            dp[i]=max(freqDict[i]+dp[i-2], dp[i-1])
        
        return (dp[-1])

