class Solution(object):
    def isInt(self, s):
        if len(s) == 0:
            return False
        if s[0] == '+' or s[0] == '-':
            return self.isUint(s[1:])
        return self.isUint(s)

    def isUint(self, s):
        if len(s) == 0:
            return False
        numbers = "0123456789"
        for x in s:
            if x not in numbers:
                return False
        return True

    def isFloatOrInt(self, s):
        if '.' in s:
            s1, s2 = s.split('.', 1)
            if not s1 and not s2:
                return False
            return (s1 == "" or self.isUint(s1)) and (s2 == "" or self.isUint(s2))
        return self.isUint(s)

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove leading or trailing whitespace
        s = s.lstrip().rstrip()
        # handle sign
        if len(s) == 0:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]#.lstrip() "+ 1" should return False
        # handle exponent
        if 'e' in s:
            s1, s2 = s.split('e', 1)
            return self.isFloatOrInt(s1) and self.isInt(s2)
        return self.isFloatOrInt(s)


if __name__ == '__main__':
    solution = Solution()
    s = " -.1"
    print solution.isNumber(s)
