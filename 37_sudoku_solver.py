class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def getValue(self, index):
        v = (0,1,2,4,8,16,32,64,128,256,511)
        return v[index]

    def changeSudoToIntInit(self, board):
        board2 = [self.getValue(10)]*81
        unique = []
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    board2[i*9+j] = -self.getValue(int(board[i][j]))
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    unique2, flag = self.setValueAt(board2, i, j, -self.getValue(int(board[i][j])))
                    unique += unique2
        return board2, unique

    def setValueAt(self, board2, i, j, value):
        board2[i*9+j] = value
        unique = []
        for m in range(0, 9):
            if board2[i*9 + m] > 0:
                new_value = board2[i*9 + m] & (511+value)
                if not new_value:
                    return [], False
                if new_value & (new_value - 1) == 0 and new_value != board2[i*9 + m]:
                    unique.append(i*9+m)
                board2[i*9 + m] = new_value
            if board2[m*9 + j] > 0:
                new_value = board2[m*9 + j] & (511+value)
                if not new_value:
                    return [], False
                if new_value & (new_value - 1) == 0 and new_value != board2[m*9 + j]:
                    unique.append(m*9+j)
                board2[m*9 + j] = new_value
            if board2[(i/3*3+m/3)*9+ j/3*3+m%3] > 0:
                new_value = board2[(i/3*3+m/3)*9+ j/3*3+m%3] & (511+value)
                if not new_value:
                    return [], False
                if new_value & (new_value - 1) == 0 and\
                    new_value != board2[(i/3*3+m/3)*9+ j/3*3+m%3]:
                    unique.append((i/3*3+m/3)*9+ j/3*3+m%3)
                board2[(i/3*3+m/3)*9+ j/3*3+m%3] = new_value
        return unique, True

    def solveSudoWithCertain(self, board2, unique):
        while unique:
            index = unique.pop()
            unique2, flag = self.setValueAt(board2,index/9,index%9, -board2[index])
            if not flag:
                return flag
            unique += unique2
        return True

    def checkSolved(self, board2):
        for i in range(0, 81):
            if board2[i] > 0:
                return i
            elif board2[i] == 0:
                return -2
        return -1

    def trySudoAt(self, board2, index, tryValue):
        if tryValue == 10:
            return False
        store_board = board2[:]
        if not board2[index] & self.getValue(tryValue):
            return self.trySudoAt(board2, index, tryValue+1)
        unique, flag = self.setValueAt(board2, index/9, index%9, -self.getValue(tryValue))
        if not flag:
            for i in range(0, 81):
                board2[i] = store_board[i]
            return self.trySudoAt(board2, index, tryValue+1)
        if not self.solveSudoWithCertain(board2, unique):
            for i in range(0, 81):
                board2[i] = store_board[i]
            return self.trySudoAt(board2, index, tryValue+1)
        new_index = self.checkSolved(board2)
        if new_index >= 0:
            if not self.trySudoAt(board2, new_index, 1):
                for i in range(0, 81):
                    board2[i] = store_board[i]
                return self.trySudoAt(board2, index, tryValue+1)
            else:
                return True
        elif new_index == -2:
            return False
        else:
            return True

    def changeSudoBack(self, board2, board):
        dic = {1:'1',2:'2',4:'3',8:'4',16:'5',32:'6',64:'7',128:'8',256:'9'}
        for i in range(0, 9):
            for j in range(0, 9):
                if -board2[i*9+j] in dic:
                    board[i][j] = dic[-board2[i*9+j]]

    def solveSudoku(self, board):
        board2, unique = self.changeSudoToIntInit(board)
        flag = self.solveSudoWithCertain(board2, unique)
        index = self.checkSolved(board2)
        if index >= 0:
            flag = self.trySudoAt(board2, index, 1)
        self.changeSudoBack(board2, board)

if __name__ == '__main__':
    s = Solution()
    board = ["...2...63","3....54.1","..1..398.",".......9.","...538...",".3.......",".263..5..","5.37....8","47...1..."]
    board = [list(l) for l in board]
    s.solveSudoku(board)
    print board