class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(0, n):
            for j in range(0, n - i):
                matrix[i][j], matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1], matrix[i][j]

        for i in range(0, n/2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
            #for j in range(0, n):
            #    matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

if __name__ == '__main__':
    solution = Solution()
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    print solution.rotate(nums)
    print nums