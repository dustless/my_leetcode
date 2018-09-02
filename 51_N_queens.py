class Solution:
    # @return a list of lists of string
    def check(self, index, i, j):
        for x in range(0, i):
            if j == index[x] or abs(index[x]-j) == i-x:
                return False
        return True

    def solveNQueens(self, n):
        index = [-1]*n
        index_list = []
        i = 0
        while i < n:
            j = index[i] + 1
            while j < n:
                if self.check(index, i, j):
                    break
                j += 1

            if j == n:
                index[i] = -1
                i -= 1
                if i == -1:
                    break
            else:
                index[i] = j
                if i == n - 1:
                    index_list.append(index[:])
                else:
                    i += 1
        result = []
        for l in index_list:
            board = []
            for j in l:
                board.append('.'*j+'Q'+'.'*(n-j-1))
            result.append(board)
        return result

if __name__ == '__main__':
    solution = Solution()
    n = 4
    print solution.solveNQueens(n)
