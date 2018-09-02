class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        i = 0
        ln = len(nums)
        if ln == 0:
            return 1
        while i < ln:
            if 0 < nums[i] <= ln and nums[i] != nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            else:
                i += 1

        for i in range(0,ln):
            if nums[i] != i+1:
                return i+1
        return nums[-1] + 1


if __name__ == '__main__':
    s = Solution()
    nums = [1,3,2,4]
    print s.firstMissingPositive(nums)