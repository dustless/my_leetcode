class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        result = []
        visited = []
        for i in range(0, m):
            visited.append([0]*n)
        i = 0
        j = 0
        while True:
            flag = False
            while j < n:
                if not visited[i][j]:
                    result.append(matrix[i][j])
                    visited[i][j] = 1
                    flag = True
                else:
                    break
                j += 1
            j -= 1
            i += 1
            while i < m:
                if not visited[i][j]:
                    result.append(matrix[i][j])
                    visited[i][j] = 1
                    flag = True
                else:
                    break
                i += 1
            i -= 1
            j -= 1

            while j >= 0:
                if not visited[i][j]:
                    result.append(matrix[i][j])
                    visited[i][j] = 1
                    flag = True
                else:
                    break
                j -= 1
            j += 1
            i -= 1
            while i >= 0:
                if not visited[i][j]:
                    result.append(matrix[i][j])
                    visited[i][j] = 1
                    flag = True
                else:
                    break
                i -= 1
            i += 1
            j += 1
            if not flag:
                break
        return result

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3]]
    print solution.spiralOrder(matrix)