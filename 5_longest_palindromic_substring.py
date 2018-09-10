class Solution:
    # @return a string
    def longestPalindrome(self, s):
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        Len = [0] * n
        P = 1
        C = 1
        for i in range(1, n - 1):
            if i < P:
                Len[i] = min(P - i, Len[2 * C - i])

            while T[i + 1 + Len[i]] == T[i - 1 - Len[i]]:
                Len[i] += 1
            if i + Len[i] > P:
                P = i + Len[i]
                C = i
        maxL, i = max((n, i) for i, n in enumerate(Len))
        return s[(i - maxL) / 2: (i + maxL) / 2]


if __name__ == "__main__":
    print Solution().longestPalindrome("xcbbcd")