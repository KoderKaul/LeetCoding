class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<k:
            return -1
        if k == 1: return nums
        # dictt = {}
        results=[]

        prev=False
        for i in range(len(nums)-k+1):
            if not prev:
                j=i+1
                while j < i+k:
                    if nums[j]-(j-i) == nums[i]:
                        j+=1
                        continue
                    else:
                        prev=False
                        results.append(-1)
                        break
                else:
                    prev=True
                    results.append(nums[j-1])
            else:
                if nums[i+k-1]-(k-1) == nums[i]:
                    prev=True
                    results.append(nums[i+k-1])
                else:
                    prev=False
                    results.append(-1)
        return results