class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        miss=1
        i=0
        n=sum(coins)
        while miss<=n:
            if i < len(coins) and coins[i]<=miss:
                miss+=coins[i]
                i+=1
            else:
                break
        return miss
