class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        # a,b = int(n/2)-1, int(n/2)
        # dp = [[float("inf")]*3 for _ in range(n)]
        # for i in range(a+1):
        #     ai = a - i
        #     bi = b + i

        #     for j in range(3):
        #         for k in range(3):
        #             if j != k:
        #                 if ai != bi - 1:
        #                     dp[ai][j] = min(
        #                         dp[ai][j],
        #                         cost[ai][j] + cost[bi][k] +
        #                         min(dp[ai + 1][c] for c in range(3) if c != j)
        #                     )
        #                     dp[bi][j] = min(
        #                         dp[bi][j],
        #                         cost[bi][j] + cost[ai][k] +
        #                         min(dp[bi - 1][c] for c in range(3) if c != j)
        #                     )
        #                 else:
        #                     dp[ai][j] = min(
        #                         dp[ai][j],
        #                         cost[ai][j] + cost[bi][k]
        #                     )
        #                     dp[bi][j] = min(
        #                         dp[bi][j],
        #                         cost[bi][j] + cost[ai][k]
        #                     )

        # return max(min(dp[0]), min(dp[-1]))
        ##cant do iterative because we have two variables to care for
        # foldedcost=[]
        # for i in range(n//2):
        #     foldedcost.append([cost[i], cost[n-i-1]])
        # cost = foldedcost

        # n=n//2
        # @lru_cache
        # def helper(i, a, b):
        #     if i==n:
        #         return 0
        #     ans = float("inf")
        #     for x in range(3):
        #         for y in range(3):
        #             if x!=a and y!=b and x!=y:
        #                 ans = min(ans, cost[i][0][x] + cost[i][1][y] + helper(i+1,x,y))
        #     return ans
        
        # return helper(0,-1,-1)

        dp = [dict() for _ in range(n // 2 + 1)]

        options = dict()
        for i in range(3):
            for j in range(3):
                if j == i:
                    continue
                k = 3 - (i + j)
                options[(i, j)] = [(j, i), (j, k), (k, i)]

        for i in range(n // 2):
            for k, v in options.items():
                dp[i + 1][k] = (
                    min(dp[i].get(x, 0) for x in v)
                    + cost[i][k[0]]
                    + cost[n - 1 - i][k[1]]
                )
        return min(dp[-1].values())