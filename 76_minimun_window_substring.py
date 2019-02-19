class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = len(s)
        lt = len(t)
        if lt == 1:
            return t if t in s else ""
        if ls < lt:
            return ""

        not_satisfied = {}
        need_satisfy = {}
        for i, c in enumerate(t):
            if c not in not_satisfied:
                not_satisfied[c] = 1
                need_satisfy[c] = 1
            else:
                not_satisfied[c] += 1
                need_satisfy[c] += 1

        left, right = 0, 0
        result = ""
        min_len = ls + 1
        satisfied_num = 0
        match_count = {}
        while right < ls:
            c = s[right]
            if c in need_satisfy:
                if c not in match_count:
                    match_count[c] = 1
                else:
                    match_count[c] += 1
                if not_satisfied.get(c, 0) > 0:
                    not_satisfied[c] -= 1
                    satisfied_num += 1
                if satisfied_num == lt:
                    while left < right:
                        rc = s[left]
                        if rc in need_satisfy:
                            match_count[rc] -= 1
                            if match_count[rc] < need_satisfy[rc]:
                                not_satisfied[rc] += 1
                                satisfied_num -= 1
                                if right - left + 1 < min_len:
                                    result = s[left:right+1]
                                    min_len = right - left + 1
                                left += 1
                                break
                        left += 1
            right += 1
        return result



if __name__ == "__main__":
    print Solution().minWindow("aa", "aa")
