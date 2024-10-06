class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        wanted = {}
        for ss in t:
            if ss not in wanted:
                wanted[ss]=0
            wanted[ss]+=1
        
        wantedLen=len(wanted.keys())
        minLen=float("inf")
        started=False
        ans=""
        total=0
        l,r=0,0
        while(l<=r and r<len(s)):
            if total < wantedLen:
                if s[r] in wanted:
                    wanted[s[r]]-=1
                    if wanted[s[r]] == 0:
                        total+=1
                r+=1
            while (total == wantedLen) and l!=r:
                if minLen >= r-l:
                    minLen=r-l
                    ans = s[l:r]
                if s[l] in wanted:
                    if wanted[s[l]] == 0:
                        total-=1
                    wanted[s[l]]+=1
                l+=1
        return ans