class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}

    def nextPermutation(self, num):
        l = len(num)
        i = l - 1
        while i > 0 and num[i] <= num[i - 1]:
            i -= 1

        if i == 0:
            num[:] = num[::-1]
            return False
        elif i == l - 1:
            num[i - 1], num[i] = num[i], num[i - 1]
        else:
            j = l - 1
            while num[i - 1] >= num[j]:
                j -= 1
            num[i - 1], num[j] = num[j], num[i - 1]
            num[i:] = num[l - 1:i - 1:-1]
        return True

    def permuteUnique(self, nums):
        nums.sort()
        result = [nums[:]]
        while self.nextPermutation(nums):
            result.append(nums[:])
        return result

if __name__ == '__main__':
    solution = Solution()
    nums = [2,1,1]
    print solution.permuteUnique(nums)
