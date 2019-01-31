class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        sub_str_map = {}
        l = len(s)
        for i in range(0, l - 9):
            sub_str = s[i:i+10]
            if sub_str in sub_str_map:
                if sub_str_map[sub_str] == 1:
                    result.append(sub_str)
                sub_str_map[sub_str] += 1
            else:
                sub_str_map[sub_str] = 1
        return result

if __name__ == '__main__':
    solution = Solution()
    s = "AAAAAAAAAAA"
    print(len(s))
    print solution.findRepeatedDnaSequences(s)

