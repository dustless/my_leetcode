class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        n = len(nums)
        if n == 1:
            return True
        i = 0
        while i < n - 1:
            if nums[i] == 0:
                j = i - 1
                while j >= 0:
                    if nums[j] > i - j:
                        break
                    j -= 1
                if j == -1:
                    return False
                i += 1
            else:
                i += nums[i]
        return True

if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,0,4]
    print solution.canJump(nums)