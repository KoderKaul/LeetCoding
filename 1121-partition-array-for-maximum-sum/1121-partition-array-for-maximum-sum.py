class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @lru_cache(None)
        def partitioning(size, maxTillNow, idx):
            # nonlocal maxSum

            if idx == len(arr):
                return size*maxTillNow 

            sumIfNotTaken = 0
            if size != 0:
                sumIfNotTaken = partitioning(0,-1,idx)+ size*maxTillNow
            if arr[idx] >= maxTillNow:
                maxTillNow = arr[idx]
            if size==k-1:
                return max((partitioning(0,-1,idx+1) + maxTillNow*k), sumIfNotTaken)

            return max(partitioning(size+1, maxTillNow, idx+1),sumIfNotTaken)



        return partitioning(0, -1, 0)