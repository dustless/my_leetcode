class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            m, n = n, m
        x = 1
        for i in range(n, m + n - 1):
            x *= i
        y = 1
        for i in range(1, m):
            y *= i
        return x/y


print Solution().uniquePaths(7, 3)
