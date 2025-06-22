class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        left = 0
        n = len(nums)
        dp = [1] + [0]*n
        MOD = 10**9+7
        minq, maxq = deque(), deque()

        acc = 1

        for right in range(n):
            num = nums[right]
            while minq and nums[minq[-1]] >  num:
                minq.pop()
            while maxq and nums[maxq[-1]] < num:
                maxq.pop()

            minq.append(right)
            maxq.append(right)

            while nums[maxq[0]] - nums[minq[0]] > k:
                acc = (acc - dp[left])%MOD
                left += 1

                if minq[0] < left:
                    minq.popleft()
                if maxq[0] < left:
                    maxq.popleft()

            dp[right+1] = acc
            acc = (acc*2)%MOD #jitne sets hain uska double ho jaega. empty set pehle se accounted hai dp[0]=1
        return dp[n]