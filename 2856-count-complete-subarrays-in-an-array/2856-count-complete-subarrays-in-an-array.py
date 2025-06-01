class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        freqMap={}

        for i in nums:
            freqMap[i]=1

        distinctNums = freqMap.keys()

        l=0
        r=0
        windowMap=defaultdict(int)
        res=0
        while l<=r and r<=len(nums):
            if len(windowMap) < len(distinctNums):
                if r==len(nums):
                    break
                windowMap[nums[r]]+=1
                r+=1
                if len(windowMap) == len(distinctNums):
                    res += len(nums) - r + 1

            elif len(windowMap) == len(distinctNums):
                windowMap[nums[l]]-=1
                if windowMap[nums[l]]<=0:
                    del windowMap[nums[l]]
                else:
                    res+= len(nums) - r + 1
                l+=1
                

        return res



        