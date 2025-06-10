class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k-=1

        while k > 0:
            steps = self.__count_steps(n, curr, curr+1)

            if k>=steps:
                k-=steps
                curr+=1
            else:
                k-=1
                curr*=10
            
        return curr

    def __count_steps(self, n, prefix1, prefix2):
        steps=0
        while prefix1<=n:
            steps+= min(n+1, prefix2) - prefix1
            prefix1*=10
            prefix2*=10
        
        return steps
