class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        word_index = 0
        words_len = len(words)
        while word_index < words_len:
            line_width = -1
            line_words = []
            while True:
                if word_index >= words_len:
                    break
                current_word_width = len(words[word_index])
                if line_width + current_word_width + 1 <= maxWidth:
                    line_words.append(words[word_index])
                    line_width += current_word_width + 1
                    word_index += 1
                else:
                    break

            # handle last line
            if word_index >= words_len:
                line_str = ' '.join(line_words)
                line_str += ' ' * (maxWidth - len(line_str))
                lines.append(line_str)
            else:
                line_words_num = len(line_words)
                line_str = line_words[0]
                total_space_num = maxWidth - line_width
                if line_words_num == 1:
                    line_str += ' ' * total_space_num
                else:
                    average_space_num = total_space_num / (line_words_num - 1)
                    extra_space_num = total_space_num - average_space_num * (line_words_num - 1)
                    for i in range(1, line_words_num):
                        if i <= extra_space_num:
                            line_str += ' ' * (average_space_num + 2) + line_words[i]
                        else:
                            line_str += ' ' * (average_space_num + 1) + line_words[i]
                lines.append(line_str)

        return lines


if __name__ == "__main__":
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    print Solution().fullJustify(words, maxWidth)
