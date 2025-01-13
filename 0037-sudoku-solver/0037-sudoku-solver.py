class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        empty = []
        for col in range(9):
            for row in range(9):
                if board[row][col] == '.':
                    empty.append((row,col))
        # vis = {}
        # emptys=len(empty)
        @cache
        def checker(row,col,val,temp):

            rowSection = row // 3
            colSection = col // 3

            for i in range(rowSection*3, 3*rowSection +3):
                for j in range(colSection*3, 3*colSection +3):
                    if val == temp[i][j]:
                        return True
            for i in range(9):
                if val == temp[i][col] or val == temp[row][i]:
                    return True
            return False
        def solver(i,j,board,emptys):
            for nums in range(1,10):
                if not checker(i,j,str(nums),board):
                    board[i][j] = str(nums)
                    emptys-=1
                    if emptys == 0:
                        return 0
                    for (r,c) in empty:
                        # board[i][j] = chr(nums + ord("0"))

                        if board[r][c] != '.':
                            continue
                        else:
                            k = solver(r,c,board,emptys)
                            if k == -1:
                                board[r][c] = '.'
                                emptys+=1
                                break
                            elif k == 0:
                                return 0
            
            board[i][j] = '.'
            return -1

        solver(empty[0][0],empty[0][1],board,len(empty))