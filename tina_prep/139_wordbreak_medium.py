class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakRecur(s: str, word_dict: Set[str], start: int):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
            return False

        return wordBreakRecur(s, set(wordDict), 0)

# Time: O(2^n) given a string of length n, there are n + 1 ways to split it into two parts.  At each step we have a choice to split or not to split.  In the worse case, when all choices are to be checked, that results in O(2^n).

# Space: O(n).  The depth of the recursion tree can go upto n.

# input: string, dictionary of words
# output: boolean of whether that string can be broken into words from wordDict

# initially seems like a DP problem where you try one word, slice the rest of the string, and continue
# use recursion and backtracking.  For finding the solution, check every possible prefix of that string in the dictionary of words
# if it is found in the dictionary, then the recursive function is called for the remaining portion of that string.
# If in some function call it is found that the complete string is in dictionary, then it will return true

# We can use memoization where an array memo is used to store the result of the subproblems.  Now, when the function is called again for a particular string, value will be fetched and returned using the memo array, if its value has been already evaluated.

# With memoization many redundant subproblems are avoided and recursion tree is pruned and thus it reduces the time complexity by a large factor

# class Solution:
#     def wordBreak(self, s:str, wordDict: List[str]) -> bool:
#         @lru_cache
#         def wordBreakMemo(s: str, word_dict: FrozenSet[str], start: int):
#             if start == len(s):
#                 return True
#             for end in range(start + 1, len(s) + 1):
#                 if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
#                     return True
#             return False

#         return wordBreakMemo(s, frozenset(wordDict), 0)
