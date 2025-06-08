class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.segTree=[0]*(2*self.n)
        self.__buildTree(nums)

    def __buildTree(self, nums):
        n = self.n
        for i in range(n):
            self.segTree[n+i] = nums[i]

        for i in range(n-1,0,-1):
            self.segTree[i] = self.segTree[2*i] + self.segTree[2*i + 1]

    def update(self, index: int, val: int) -> None:
        pos = index + self.n
        self.segTree[pos] = val

        while pos>1:
            pos//=2
            self.segTree[pos]=self.segTree[2*pos]+self.segTree[2*pos+1]


    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        total=0
        while left <= right:
            if left % 2 == 1:
                total+=self.segTree[left]
                left+=1
            if right % 2 == 0:
                total+=self.segTree[right]
                right-=1

            left//=2
            right//=2
        return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)