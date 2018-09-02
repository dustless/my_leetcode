class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        lh = len(height)
        if lh < 3:
            return 0
        left_max = [height[0]] * lh
        right_max = [height[-1]] * lh
        result = 0
        i = 1
        while i < lh:
            if height[i] <= left_max[i-1]:
                left_max[i] = left_max[i-1]
            else:
                left_max[i] = height[i]
            i += 1
        i = lh - 2
        while i >= 0:
            if height[i] <= right_max[i+1]:
                right_max[i] = right_max[i+1]
            else:
                right_max[i] = height[i]
            i -= 1

        for i in range(1, lh-1):
            result += min(left_max[i], right_max[i]) - height[i]

        return result



if __name__ == '__main__':
    s = Solution()
    height = [5,3,1,4]
    print s.trap(height)