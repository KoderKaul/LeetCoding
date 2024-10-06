class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        wanted = {}
        # wanted2 = {}
        for ss in t:
            if ss not in wanted:
                wanted[ss]=0
                # wanted2[ss]=0

            wanted[ss]+=1
            # wanted2[ss]+=1
        
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
            # elif total == wantedLen:
            #     if minLen >= r+1-l:
            #         minLen=r+1-l
            #         ans = s[l:r+1]
            while (total == wantedLen) and l!=r:
                if minLen >= r-l:
                    minLen=r-l
                    ans = s[l:r]
                if s[l] in wanted:
                    if wanted[s[l]] == 0:
                        total-=1
                    wanted[s[l]]+=1
                l+=1




            # print(l,r,wanted,total,s[l],s[r])
            # if s[r] in wanted and wanted[s[r]]>0:
            #     started=True
            #     wanted[s[r]]-=1
            #     # print(wanted[s[r]])
            #     if wanted[s[r]] == 0:
            #         total+=1
            #         # print(total)
            #         if total == wantedLen:
            #             # print(minLen,l,r,r+1-l)
            #             if minLen >= r+1-l:
            #                 minLen=r+1-l
            #                 ans = s[l:r+1]
            #     r+=1
                
            # else:
            #     if s[r] not in wanted:
            #         if not started:
            #             l+=1
            #         r+=1
            #     elif wanted[s[r]] == 0:
            #         while (s[l] not in wanted or wanted[s[r]] <=0) and l!=r:
            #             print(l)
            #             if s[l] in wanted:
            #                 if wanted[s[l]] == 0:
            #                     total-=1
            #                 wanted[s[l]]+=1
            #             l+=1
        # if total == wantedLen:
        #     # print(minLen,l,r,r+1-l)
        #     if minLen >= r+1-l:
        #         minLen=r+1-l
        #         ans = s[l:r+1]
        return ans