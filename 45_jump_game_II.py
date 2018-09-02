class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1
        weight = [num + i for i, num in enumerate(nums)]
        jumps = 1
        next_index = 0
        while True:
            if nums[next_index] >= len(nums) - next_index - 1:
                return jumps
            optimal_index = next_index+1
            max_weight = weight[next_index+1]
            for i in range(next_index+1, next_index+1+nums[next_index]):
                if weight[i] > max_weight:
                    optimal_index = i
                    max_weight = weight[i]
            next_index = optimal_index
            jumps += 1





if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,1,4]
    print solution.jump(nums)