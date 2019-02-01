# time limit exceeded
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#         result = []
#         for word in wordDict:
#             if s.startswith(word):
#                 if s == word:
#                     result.append(word)
#                 else:
#                     rest = self.wordBreak(s[len(word):], wordDict)
#                     if not rest:
#                         continue
#                     for item in rest:
#                         result.append(word + " " + item)
#         return result

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#         result = []
#         ls = len(s)
#         lw = len(wordDict)
#         wordLen = [len(word) for word in wordDict]
#         i = 0
#         path = []
#         j = 0
#         while True:
#             while j < lw:
#                 if s[i:i+wordLen[j]] == wordDict[j]:
#                     path.append(j)
#                     if i+wordLen[j] == ls:
#                         wordList = [wordDict[x] for x in path]
#                         result.append(' '.join(wordList))
#                     i += len(wordDict[j])
#                     j = 0
#                     break
#                 j += 1
#             if j == lw:
#                 if path:
#                     j = path.pop(-1)
#                     i -= len(wordDict[j])
#                     j += 1
#                 else:
#                     break
#         return result

# time limit exceeded
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = {}
        def breakWord(s):
            tmp_res = []
            for word in wordDict:
                if s.startswith(word):
                    if s == word:
                        tmp_res.append(word)
                    else:
                        tail = s[len(word):]
                        if tail not in result:
                            rest = breakWord(tail)
                        else:
                            rest = result[tail]
                        if not rest:
                            continue
                        for item in rest:
                            tmp_res.append(word + " " + item)
            if s not in result:
                result[s] = tmp_res
            return tmp_res

        breakWord(s)
        return result[s]


if __name__ == '__main__':
    solution = Solution()
    s = "aaaaa"
    wordDict = ["a","aa","aaa"]
    print solution.wordBreak(s, wordDict)
