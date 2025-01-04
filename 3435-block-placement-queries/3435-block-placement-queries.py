class Solution:    
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        bit, res = [0] * (min(50000, 3 * len(queries)) + 1), []
        
        def bit_range(p, down=True):
            while p >= 0 and p < len(bit):
                yield p
                p = (p & (p + 1)) - 1 if down else p | (p + 1)
        
        def get_max(p: int) -> int:
            return max(bit[i] for i in bit_range(p))
        
        def update(p, val):
            for idx in bit_range(p, False):
                bit[idx] = max(bit[idx], val)
        
        blocks = [0] + sorted([x for t, x, *sz in queries if t == 1])
        for i, b in enumerate(blocks[1:]):
            update(b, b - blocks[i])
        
        for t, x, *sz in reversed(queries):
            p = bisect_left(blocks, x)
            if t == 1:
                if p + 1 < len(blocks):
                    update(blocks[p + 1], blocks[p + 1] - blocks[p - 1])
                del blocks[p]
            else:
                res.append(x - blocks[p - 1] >= sz[0] or get_max(x) >= sz[0])
        
        return (res[::-1])
