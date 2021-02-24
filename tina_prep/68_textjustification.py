class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(line, width, maxWidth):
            if len(line) == 1:
                return line[0] + ' ' * (maxWidth - width)
            else:
                spaces = maxWidth - width
                locations = len(line) - 1
                assign = locations * [spaces // locations]
                for i in range(spaces % locations):
                    assign[i] += 1
                s = ''
                for i in range(locations):
                    s += line[i] + assign[i] * ' '
                s += line[-1]
                return s

        answer = []
        line, width = [], 0
        for w in words:
            if width + len(w) + len(line) <= maxWidth:
                line.append(w)
                width += len(w)
            else:
                answer.append(justify(line, width, maxWidth))
                line, width = [w], len(w)
        answer.append(' '.join(line) + (maxWidth -
                                        width - len(line) + 1) * ' ')
        return answer

# I have no idea how this actually works, I just found it on the discussion board.

# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         i = 0
#         N = len(words)
#         result = []

#         while i < N:
#             # decide how many words to put in one line
#             oneLine = [words[i]]
#             j = i + 1
#             currWidth = len(words[i])
#             positionNum = 0
#             spaceNum = maxWidth - len(words[i])
#             while j < N and currWidth + 1 + len(words[j]) <= maxWidth:
#                 oneLine.append(words[j])
#                 currWidth += 1 + len(words[j])
#                 spaceNum -= len(words[j])
#                 positionNum = positionNum + 1
#                 j = j + 1
#             i = j
#             # decide the layout of one line
#             if i < N and positionNum:
#                 spaces = [' ' * (spaceNum / positionNum + (k < spaceNum % positionNum)) for k in range(positionNum)] + ['']
#             else: # last line or the line only has one word
#                 spaces = [' '] * positionNum + [' ' * (maxWidth - currWidth)]
#             result.append(''.join([s for pair in zip(oneLine, spaces) for s in pair]))
#         return result


# can we not just count the number of letters in each word, and try to add them together adding one for the space padding?
# oh, well we need to cosnider the possibility that leftover words will have lots of spaces, and we want to set up the words properly
# this will probably be a dynamic programming approach.
