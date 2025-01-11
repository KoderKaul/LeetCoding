class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        n=len(heights)
        l_nse=[-1]*n
        r_nse=[n]*n
        heights.append(-1)
        for i in range(n+1):
            while s and heights[s[-1]] > heights[i]:
                r_nse[s[-1]]=i
                s.pop()

            if s:
                l_nse[i]=s[-1]

            s.append(i)
        mArea=0
        # print(r_nse, l_nse, s)
        for i in range(n):
            mArea=max(mArea, heights[i]*(r_nse[i]-l_nse[i]-1))
        return mArea