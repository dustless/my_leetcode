class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def doCombinationSum(self, candidates, target):
        if not candidates:
            return []
        if target < candidates[0]:
            return []
        result = []
        i = 0
        while i*candidates[0] <= target:
            pre = [candidates[0]]*i
            if target == i*candidates[0]:
                result += [pre]
            else:
                temp = self.doCombinationSum(candidates[1:], target-i*candidates[0])
                if len(temp):
                    for l in temp:
                        result += [pre + l]
            i += 1
        return result

    def combinationSum(self, candidates, target):
        candidates.sort()
        result = self.doCombinationSum(candidates, target)
        return result

if __name__ == '__main__':
    s = Solution()
    candidates = [2,3,6]
    target = 6
    print s.combinationSum(candidates, target)