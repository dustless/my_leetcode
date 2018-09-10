class Solution:
    # @param S, a string
    # @param L, a string[]
    # @return an integer[]
    def findSubstring(self, S, L):
        if len(L) == 0 or len(S) < len(L) * len(L[0]):
            return []
        l = len(S)
        ll = len(L)
        wl = len(L[0])
        sl = ll * wl
        result = []
        dic = {}

        for i in range(0, ll):
            if L[i] in dic:
                dic[L[i]] += 1
            else:
                dic[L[i]] = 1

        i = 0
        while i <= l - sl:
            sub = S[i:i + sl]
            dic2 = dic.copy()
            while sub[0:wl] in dic2:
                dic2[sub[0:wl]] -= 1
                if dic2[sub[0:wl]] < 0:
                    break
                sub = sub[wl:]
                if len(sub) == 0:
                    result.append(i)
                    break
            i += 1
        return result


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print Solution().findSubstring(s, words)
