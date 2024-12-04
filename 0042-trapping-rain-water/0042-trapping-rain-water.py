class Solution:
    def trap(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        leftMax, rightMax=h[l],h[r]

        water=0
        while l<=r:
            if leftMax<rightMax:
                if h[l]>leftMax:
                    leftMax=h[l]
                else:
                    water+= leftMax-h[l]
                l+=1
            else:
                if h[r]>rightMax:
                    rightMax=h[r]
                else:
                    water+= rightMax-h[r]
                r-=1
        return water

