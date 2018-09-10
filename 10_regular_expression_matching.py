class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        ls = len(s)
        lp = len(p)
        if lp == 0:
            return ls == 0
        if ls == 0:
            return lp > 1 and p[1] == '*' and self.isMatch(s, p[2:])

        if lp == 1:
            return ls == 1 and (s[0] == p[0] or p[0] == '.')

        if s[-1] != p[-1] and p[-1] != '*' and p[-1] != '.':
            return False

        if p[1] == '*':
            return self.isMatch(s, p[2:]) or (
                        (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:],
                                                                       p))
        else:
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])


if __name__ == "__main__":
    print Solution().isMatch("aab", "c*a*b")
