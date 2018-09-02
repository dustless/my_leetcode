class Solution:
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    def groupAnagrams(self, strs):
        result = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in result:
                result[key] = [str]
            else:
                result[key].append(str)
        return result.values()

if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print solution.groupAnagrams(strs)