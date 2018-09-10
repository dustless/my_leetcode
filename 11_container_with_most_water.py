class Solution:
    # @return an integer
    def maxArea(self, height):
        l = len(height)
        left = 0
        right = l - 1
        max_area = 0
        while (left < right):
            max_area = max(max_area,
                           min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


print Solution().maxArea([1,8,6,2,5,4,8,3,7])
