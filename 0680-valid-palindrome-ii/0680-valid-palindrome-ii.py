class Solution:
    def validPalindrome(self, s: str,l=0, r=-1, subs=0) -> bool:
        if r==-1:
            r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                if subs!=0:
                    return False
                if r-1 >=0 and s[l]==s[r-1] and l+1 <= len(s)-1 and s[l+1]==s[r]:
                    return self.validPalindrome(s,l+1,r,1) or self.validPalindrome(s,l,r-1,1) 
                elif r-1 >=0 and s[l]==s[r-1]:
                    subs=1
                    r-=1
                elif l+1 <= len(s)-1 and s[l+1]==s[r]:
                    subs=1
                    l+=1
                else:
                    return False
            else:
                l+=1
                r-=1
        return True