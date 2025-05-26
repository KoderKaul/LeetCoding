class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n, stack = len(heights), []
        ans = [0]*n

        for i, h in enumerate(reversed(heights)):
            while stack and h > stack[-1]:
                stack.pop()
                ans[i]+=1

            if stack:
                ans[i]+=1

            stack.append(h)

        return ans[::-1]
