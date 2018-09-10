class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        min_sums = []
        for i in range(0, m):
            min_sums.append([0] * n)

        min_sums[0][0] = grid[0][0]
        for j in range(1, n):
            min_sums[0][j] = min_sums[0][j-1] + grid[0][j]
        for i in range(1, m):
            min_sums[i][0] = min_sums[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                min_sums[i][j] = min(min_sums[i-1][j], min_sums[i][j-1]) + grid[i][j]
        return min_sums[-1][-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print Solution().minPathSum(grid)