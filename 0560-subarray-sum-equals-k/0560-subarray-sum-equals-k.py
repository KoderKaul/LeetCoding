class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum=0

        sum_till_idx = {0:1}
        count=0
        for i,n in enumerate(nums):
            # if n==k:
            #     count+=1
            prefixSum+=n
            # print(n,i,sum_till_idx)
            # if prefixSum==k:
                # count+=1
            if prefixSum-k in sum_till_idx:
                count+=(sum_till_idx[prefixSum-k])
            
            if prefixSum not in sum_till_idx:
                sum_till_idx[prefixSum]=1
            else:
                sum_till_idx[prefixSum]+=1
        return count