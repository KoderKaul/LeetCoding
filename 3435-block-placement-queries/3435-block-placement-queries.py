class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        bit, res = [0] * (min(50000, 3 * len(queries)) + 1), []

        def query(p: int) -> int:
            """Get the maximum value in the Fenwick Tree up to index p."""
            ans = 0
            while p > 0:
                ans = max(ans, bit[p])
                p -= (p & -p)
            return ans

        def update(p: int, val: int):
            """Update the Fenwick Tree with value `val` at index p."""
            while p < len(bit):
                bit[p] = max(bit[p], val)
                p += (p & -p)

        blocks = [0] + sorted([x for t, x, *sz in queries if t == 1])
        # keep track of the gaps between blocks
        for i in range(1, len(blocks)):
            # Subtracting current block from the previous block
            update(blocks[i], blocks[i] - blocks[i - 1])

        #sari obstacles dal do fir ulti queries accept karo
        #jabh type 1 aaega us time apn, us block ko remove kardenge using delete
        # and next block ko update kardenge with new prev i.e curr ka prev so val=nxt-prev for nxt index
        #in type2, you query 2 things - your x ka gap and the gap between x and prev => before prev or between x and prev you can put
        for t, x, *sz in reversed(queries):
            if t == 1:
                idx = bisect_left(blocks, x) # this will definately exist since we only added them 
                prev, nxt = blocks[idx - 1], blocks[idx + 1] if idx + 1 < len(blocks) else len(bit)
                del blocks[idx]
                update(nxt, nxt - prev)
            else:
                idx = bisect_left(blocks, x)
                prev_block = blocks[idx - 1]
                # prev ka gap or x-lastBlock mein se max
                max_gap = max(query(x), x - prev_block)

                res.append(max_gap >= sz[0])

        return res[::-1]