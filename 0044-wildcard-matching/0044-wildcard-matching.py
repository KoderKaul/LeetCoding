class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        cache={}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i>=len(s) and j>=len(p):
                cache[(i,j)] = True

                return True
            if j>=len(p) :
                cache[(i,j)] = False
                return False
            if i>=len(s):
                for k in range(j, len(p)):
                    if p[k]!="*":
                        return False
                return True

            match= (p[j]=='?' or s[i]==p[j])

            if match:
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]
            
            elif p[j]=="*":
                cache[(i,j)] = dfs(i,j+1) or (  dfs(i+1,j))
                return cache[(i,j)]

            cache[(i,j)] = False
            return cache[(i,j)]
        
        return dfs(0,0)