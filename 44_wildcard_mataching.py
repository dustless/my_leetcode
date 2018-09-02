class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def matchIndex(self, s, p, start):
        ls = len(s)
        lp = len(p)
        if lp > ls:
            return -1
        if lp == 0:
            return 0
        p_list = p.split('?')
        i = start
        l = len(p_list[0])
        while True:
            i = s.find(p_list[0], i)
            if i == -1:
                return -1
            if i + lp > ls:
                return -1
            flag = True
            for j in range(l, lp):
                if p[j] != s[i+j] and p[j] != '?':
                    flag = False
                    break
            if flag:
                return i
            i += 1

    def isMatch(self, s, p):
        while '**' in p:
            p = p.replace('**', '*')
        p_list = p.split('*')
        l = len(p_list)
        ls = len(s)
        if l == 0:
            return ls == 0
        if ls == 0:
            return len(p.replace('*', '')) == 0
        if len(p.replace('*', '')) > ls:
            return False
        if l == 1 and ls != len(p):
            return False

        if self.matchIndex(s, p_list[0], 0) != 0:
            return False
        if p_list[-1]:
            if self.matchIndex(s, p_list[-1], ls-len(p_list[-1])) != ls-len(p_list[-1]):
                return False
            s = s[len(p_list[0]):ls-len(p_list[-1])]
        else:
            s = s[len(p_list[0]):]
        start = 0
        for pi in range(1, l-1):
            start = self.matchIndex(s, p_list[pi], start)
            if start == -1:
                return False
            start += len(p_list[pi])
        return True


if __name__ == '__main__':
    solution = Solution()
    s = 'abcdef'
    p = 'a?*cde*'
    print solution.isMatch(s, p)