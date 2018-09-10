class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def doCombinationSum(self, candidates, target):
        if not candidates:
            return []
        if target < candidates[0]:
            return []
        if target == candidates[0]:
            return [[candidates[0]]]
        result = []
        i = 0
        lc = len(candidates)
        while i < lc-1 and candidates[i]==candidates[i+1]:
            i += 1
        j = i + 1  # first index such than candidates[j]!=candidates[0]
        i = 0
        while i <= j:
            if target == i*candidates[0]:
                result += [[candidates[0]]*i]
            elif target > i*candidates[0]:
                temp = self.doCombinationSum(candidates[j:], target-i*candidates[0])
                if len(temp):
                    for l in temp:
                        result += [[candidates[0]]*i + l]
            else:
                break
            i += 1
        return result

    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = self.doCombinationSum(candidates, target)
        return result


print Solution().combinationSum2([10,1,2,7,6,1,5], 8)
