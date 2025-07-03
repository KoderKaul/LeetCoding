class Solution:
    def appealSum(self, s: str) -> int:
        res, cur, prev = 0, 0, defaultdict(lambda: -1)

        # new substr to include are between previous and current sighting of the chr for the appeal
        # subtrings b/w i,j = j-i
        # each character appears in (i + 1) * (n - i) substrings
        # now start se we only take substrings from prev sighting of char
        for i, ch in enumerate(s):
            res += (i - prev[ch])*(len(s)-i)
            prev[ch] = i

        return res  
            