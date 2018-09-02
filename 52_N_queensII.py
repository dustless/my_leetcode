class Solution:
    # @return a list of lists of string
    def check(self, index, i, j):
        for x in range(0, i):
            if j == index[x] or abs(index[x]-j) == i-x:
                return False
        return True

    def totalNQueens(self, n):
        index = [-1]*n
        index_list = []
        i = 0
        sum = 0
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
                    sum += 1
                else:
                    i += 1
        return sum

if __name__ == '__main__':
    solution = Solution()
    n = 5
    print solution.totalNQueens(n)
