class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        path_nums = []
        for i in range(0, m):
            path_nums.append([0] * n)

        # init
        path_nums[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for j in range(1, n):
            path_nums[0][j] = path_nums[0][j-1] if obstacleGrid[0][j] == 0 else 0
        for i in range(1, m):
            path_nums[i][0] = path_nums[i-1][0] if obstacleGrid[i][0] == 0 else 0

        # dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                path_nums[i][j] = path_nums[i-1][j] + path_nums[i][j-1] if obstacleGrid[i][j] == 0 else 0
        return path_nums[-1][-1]


obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print Solution().uniquePathsWithObstacles(obstacleGrid)
