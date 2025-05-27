class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areaMax = 0

        l,r=0, len(heights)-1
        maxheight=max(heights)
        while l<r:
            if maxheight * (r-l) <= areaMax:
                break
            areaMax =max(areaMax, min(heights[l], heights[r])*(r-l))

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1

        return areaMax