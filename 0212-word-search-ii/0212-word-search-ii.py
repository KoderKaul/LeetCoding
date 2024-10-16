class TrieNode:
    def __init__(self):
        self.children={}
        self.isWordEnd=False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr= self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr = curr.children[c]
        curr.isWordEnd=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(r, c, parent, path):
            letter = board[r][c]
            curr = parent.children[letter]

            path += letter

            if curr.isWordEnd:
                result.add(path)
                curr.isWordEnd = False
            
            board[r][c] = '#'
            for x,y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                Nr, Nc = r+x, c+y
                if 0<=Nr<len(board) and 0<=Nc<len(board[0]):
                    if board[Nr][Nc] in curr.children:
                        backtrack(Nr, Nc, curr, path)
            board[r][c] = letter

            if not curr.children:
                parent.children.pop(letter)
        result, trie = set(), Trie()
        
        for word in words:
            trie.insert(word)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.root.children:
                    backtrack(row, col, trie.root, "")

        return list(result)