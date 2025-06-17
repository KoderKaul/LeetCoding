class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # @lru_cache
        # def backtrack(j, res):
        #     nonlocal maxLen
        #     if j<0:
        #         return
        #     while j >=0:
        #         while j>=0 and s[j]=='0':
        #             j-=1
        #             res = '0'+res
        #             maxLen=max(maxLen, len(res))
        #         if j>=0 and int(str(s[j]+res),2)<=k:
        #             maxLen=max(maxLen, len(res)+1)
        #             backtrack(j-1,'1'+res)
        #         j-=1
        
        # backtrack(len(s)-1,"")
        maxLen=0

        i = len(s)-1
        value=0
        leng=0

        while i>=0:
            while i>=0 and s[i]=='0':
                i-=1
                leng+=1
                maxLen=max(maxLen,leng)
            if i>=0 and value+2**(leng) <= k:
                value += 2**(leng)
                leng+=1
                maxLen = max(maxLen,leng)

            i-=1
        return maxLen