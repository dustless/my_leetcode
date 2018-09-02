class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def generateMatrix(self, n):
        if n == 0:
            return []
        matrix = []
        for i in range(0, n):
            matrix.append([0] * n)

        i = 0
        j = 0
        k = 1
        while True:
            flag = False
            while j < n:
                if not matrix[i][j]:
                    matrix[i][j] = k
                    k += 1
                    flag = True
                else:
                    break
                j += 1
            j -= 1
            i += 1
            while i < n:
                if not matrix[i][j]:
                    matrix[i][j] = k
                    k += 1
                    flag = True
                else:
                    break
                i += 1
            i -= 1
            j -= 1

            while j >= 0:
                if not matrix[i][j]:
                    matrix[i][j] = k
                    k += 1
                    flag = True
                else:
                    break
                j -= 1
            j += 1
            i -= 1
            while i >= 0:
                if not matrix[i][j]:
                    matrix[i][j] = k
                    k += 1
                    flag = True
                else:
                    break
                i -= 1
            i += 1
            j += 1
            if not flag:
                break
        return matrix

if __name__ == '__main__':
    solution = Solution()
    n = 4
    print solution.generateMatrix(n)





