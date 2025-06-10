class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_steps(curr, n):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1  # we've already counted '1'

        while k > 0:
            steps = get_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1

        return curr