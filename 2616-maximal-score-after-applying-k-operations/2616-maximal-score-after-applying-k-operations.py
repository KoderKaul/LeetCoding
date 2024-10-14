class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in nums:
            heappush(heap,-i)
        score=0
        for i in range(k):
            top=heappop(heap)
            score+=-top
            heappush(heap,-math.ceil(abs(top)/3))
        return score