class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        sum = nums[0]
        max_sum = nums[0]
        l = len(nums)
        for i in range(1, l):
            if sum > 0:
                sum += nums[i]
            else:
                sum = nums[i]
            if sum > max_sum:
                max_sum = sum
        return max_sum

if __name__ == '__main__':
    solution = Solution()
    nums = [1,-6,2,1]
    print solution.maxSubArray(nums)