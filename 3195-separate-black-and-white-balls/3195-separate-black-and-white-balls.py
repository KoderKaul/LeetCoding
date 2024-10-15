class Solution:
    def minimumSteps(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 0
        count=0
        l=n-1
        s=(list(s))
        # print(s)
        zeroes=0
        while l >= 0:
            while l>=0 and s[l]=='1':
                count+=zeroes
                l-=1
            r=l
            while r>=0 and s[r]=='0':
                zeroes+=1
                r-=1
            # count+= zeroes
            
            # if r==0:
            #     # if s[r]=='0':
            #     #     count-= zeroes

            #     break
            # s[r],s[l]=s[l],s[r]
            l=r
        return count


        # while l<=r and r<n:
        #     if s[r]=='0':
        #         s[r],s[l]=s[l],s[r]
        #         l+=1
        #         r+=1
        #         count+=1
        #     else:
        #         r+=1
        # return count