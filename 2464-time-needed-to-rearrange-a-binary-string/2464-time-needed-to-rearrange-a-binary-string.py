class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        steps, zeroes = 0, 0
        for ch in s:
            print(zeroes, steps, ch)
            if ch == '0':
                zeroes += 1
            elif zeroes > 0:
                steps = max(1 + steps, zeroes)
            print("k",zeroes, steps, ch)
            
        return steps