class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # 2,3 5,8 6,7 6,4 
        # n = len(envelopes)
        # dp = [1 for i in envelopes]
        # for i in range(n-2,-1,-1):
        #     for j in range(i+1, n):
        #         if envelopes[i][-1] < envelopes[j][-1]:
        #             dp[i]=max(dp[i], dp[j]+1)

        # return max(dp)

        #Using binary search technique for LIS
        res=[]
        for w,h in envelopes:
            idx = bisect_left(res,h)
            if idx >= len(res):
                res.append(h)
            else:
                res[idx]=h

        return len(res)