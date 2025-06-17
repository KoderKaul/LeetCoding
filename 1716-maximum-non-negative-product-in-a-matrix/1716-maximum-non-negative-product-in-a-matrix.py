class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m,n=len(grid), len(grid[0])
        maxNum = 5**31
        minNum = -(5**31)
        dp = [[[maxNum, minNum] for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n-1] = [grid[-1][-1] if grid[-1][-1]<=0 else maxNum,grid[-1][-1] if grid[-1][-1]>=0 else minNum]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j==n-1:
                    continue

                mostNeg = min(dp[i+1][j][0], dp[i][j+1][0])
                mostPos = max(dp[i+1][j][1], dp[i][j+1][1])

                if grid[i][j] < 0:
                    dp[i][j][0] = min(dp[i][j][0], mostPos * grid[i][j])
                    dp[i][j][1] = max( dp[i][j][1], mostNeg * grid[i][j])
                else:
                    dp[i][j][0] = min(dp[i][j][0], mostNeg * grid[i][j])
                    dp[i][j][1] = max( dp[i][j][1], mostPos * grid[i][j])
        return dp[0][0][1] % (10**9+7) if  dp[0][0][1] not in [maxNum, minNum] else -1