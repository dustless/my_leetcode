class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        s_length = len(s)
        max_length = 0
        stack = []
        last = range(0, s_length)
        for i in range(0, s_length):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    index = stack.pop()
                    last[i] = index
                    if index > 0 and last[index - 1] != index - 1:
                        last[i] = last[index - 1]
                    max_length = max(max_length, i - last[i] + 1)
        return max_length


if __name__ == "__main__":
    s = ")()())"
    print Solution().longestValidParentheses(s)
