class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def check(self, board, row, colume, value):
        for i in range(0, 9):
            if board[row][i] == value:
                return False
        for i in range(0, 9):
            if board[i][colume] == value:
                return False
        for i in range(0, 3):
            for j in range(0, 3):
                if board[row/3 + i][colume/3 +j] == value:
                    return False
        return True
    
    def solveSudokuAt(self, board, row, colume):
        if row == 9:
            return True
        if board[row][colume] != '.':
            if colume == 8:
                return self.solveSudokuAt(board, row+1, 0)
            else:
                return self.solveSudokuAt(board, row, colume+1)
        for i in range(0, 9):
            char = str(i+1)
            if self.check(board, row, colume, char):
                board[row][colume] = char
                if colume == 8:
                    if self.solveSudokuAt(board, row+1, 0):
                        return True
                elif self.solveSudokuAt(board, row, colume+1):
                    return True
                board[row][colume] = '.'
        return False
    
    def solveSudoku(self, board):
        return self.solveSudokuAt(board, 0, 0)
