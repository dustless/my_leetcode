class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        l = len(num)
        i = l - 1
        while i > 0 and num[i] <= num[i - 1]:
            i -= 1

        if i == 0:
            num[:] = num[::-1]
        elif i == l - 1:
            num[i - 1], num[i] = num[i], num[i - 1]
        else:
            j = l - 1
            while num[i - 1] >= num[j]:
                j -= 1
            num[i - 1], num[j] = num[j], num[i - 1]
            num[i:] = num[l - 1:i - 1:-1]


nums = [1,2,3,5,4]
Solution().nextPermutation(nums)
print nums
