class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wildcards={}
        revwildcards={}

        def addwildcards(word):
            revwildcards[word]=[]
            for i,w in enumerate(word):
                wc = word[:i] + '_' + word[i+1:]
                if wc not in wildcards:
                    wildcards[wc] = []
                wildcards[wc].append(word)

                revwildcards[word].append(wc)


        for word in wordList:
            addwildcards(word)
        if beginWord not in wordList:
            addwildcards(beginWord)
        # else:
        #     return abs(wordList.index(beginWord) - wordList.index(endWord))
        # print(wildcards)
        q=deque()
        # for wildcards in revwildcards[endWord]:
        #     q.append(wildcards)
        q.append(endWord)
        count=0
        vis={}
        while q:
            count+=1

            for _ in range(len(q)):
                word = q.popleft()
                if beginWord == word:
                    return count
                wild = revwildcards[word]
                for cards in wild:
                    for words in wildcards[cards]:
                        if word == words or words in vis:
                            continue
                        vis[words]=True
                        q.append(words)
        return 0