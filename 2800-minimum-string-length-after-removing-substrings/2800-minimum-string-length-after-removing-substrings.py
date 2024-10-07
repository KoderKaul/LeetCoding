class Solution:
    def minLength(self, s: str) -> int:
        # abcdecabdh
        ab=cd = -1

        while True:
            try:
                ab =  s.index("AB") 
            except:
                try:
                    cd = s.index("CD")
                except:
                    return len(s)
            
            if ab != -1:
                s= s[:ab] + s[ab+2:]
                # s.pop(ab)
            if cd != -1:
                s= s[:cd] + s[cd+2:]
            
            ab=cd = -1
            


