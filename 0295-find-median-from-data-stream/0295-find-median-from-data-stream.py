class MedianFinder:

    def __init__(self):
        # odd=True
        self.stream = []
        # 2 3 4 5

    def addNum(self, num: int) -> None:
        # n = len(self.stream)
        # if n == 0:
        #     stream.append(num)
        # elif n == 1:
        #     stream.append(num)
        #     odd = False
        # elif n==2:
        #     stream.append(num)
        #     odd = True
        self.stream.append(num)
# 1234567

    def findMedian(self) -> float:
        n = len(self.stream)
        # if n == 1:
        #     return self.stream[0]
        # elif n == 2:
        #     return (self.stream[1] + self.stream[0])/2
        # print(n,n//2)
        # 1 2 3 4 5 6
        self.stream.sort()

        if n%2!=0:
            return self.stream[n//2]
        else:
            return (self.stream[n//2 - 1] + self.stream[n//2])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()