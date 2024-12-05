class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        def combos(word):
            return [word[:i]+"#"+word[i+1:] for i in range(len(word))]
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        hashes=defaultdict(list)
        combo=defaultdict(list)
        for word in wordList:
            possibleWords = combos(word)
            combo[word]=possibleWords
            for w in possibleWords:
                hashes[w].append(word)
        

        q = deque()
        q.append(beginWord)
        visited=set()
        jumps=1
        while q:
            size=len(q)
            for _ in range(size):
                word=q.popleft()
                possibleHashes= combo[word]
                visited.add(word)
                for ph in possibleHashes:
                    if ph in combo[endWord]:
                        return jumps+1
                    for wr in hashes[ph]:
                        if wr not in visited:
                            q.append(wr)
            jumps+=1
        return 0
        
            