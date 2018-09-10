class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        ed = range(0, n + 1)

        pre_ed = 0
        for i in range(1, m + 1):
            for j in range(0, n + 1):
                if j == 0:
                    pre_ed = ed[j]
                    ed[j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        pre_ed, ed[j] = ed[j], pre_ed
                    else:
                        new_ed = min(ed[j - 1], ed[j], pre_ed) + 1
                        pre_ed, ed[j] = ed[j], new_ed
        return ed[-1]


if __name__ == "__main__":
    print Solution().minDistance("intention", "execution")
