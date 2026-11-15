class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check rows:
        for row in board:
            seen = set()
            for num in row:
                if num == '.': continue
                if num in seen: 
                    return False
                seen.add(num)

        #check cols:
        for col in zip(*board):
            seen = set()
            for num in col:
                if num == '.': continue
                if num in seen: 
                    return False
                seen.add(num)


        #check each 3x3:
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()
                for r in range(box_row,box_row+3):
                    for c in range(box_col,box_col+3):
                        if board[r][c] == '.': continue
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])
        
        return True




                        

'''
Algorithm:
1.for each row:
    if there is duplicates return false
    else continue
2.for each col:
    if there is duplicates return false
    else continue
3.for both diagonals:
    if there is duplicates return false
    else continue
4.for each 3x3:
    if there is duplicates return false
    else continue
5.return true
    
'''
