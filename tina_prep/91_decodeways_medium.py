class Solution:

    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s)-1:
            return 1

        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index: index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

        return answer

    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)

# Time Complexity: O(N) where N is the length of the string.  Memoization prunes the recursion tree and decodes for an index only once.  This is linear time complexity.

# Space Complexity: O(N).  The dictionary used for memoization would take the space equal to the length of the string.  There would be an entry for each index value.


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         decodings = 0
#         prev = None
#         for ch in reversed(s):
#             if ch == "0":
#                 prev = "0"
#                 continue
#             if ch == "1" and prev != "0":
#                 prev = "1"
#                 decodings += 2
#             if ch == "2" and (prev == "1" or prev == "2" or prev == "3" or prev == "4" or prev == "5" or prev == "6"):
#                 prev = "2"
#                 decodings += 2
#             else:
#                 prev = ch
#                 decodings += 1
#         return decodings


# Input: given a string
# Output: Return how many possible encodings exist

# note, we don't need to calculate the actual encodings, we just need to determine the possibilities

# note that a number can be decoded multiple ways if and only if it starts with 1 or 2.  In particular, a number can be decoded in 2 possible ways if it starts with 1, unless it ends with 0.

# If we run into a 2, we can decode in 2 possible ways as long as the next number is from 1-6.

# a number cannot begin with 0, meaning that if we see a 0, there is really only one way to encode it and the number before it.

# consider traversing the string, either from the beginning or from the end (more likely the end actually)
# if we run upon a zero, we don't update the number of decodings
# if we run upon a number from 3-9, we add 1 to the number of possible decodings
# if we run upon a 1 or a 2, we add 2 to the number of possible decodings
