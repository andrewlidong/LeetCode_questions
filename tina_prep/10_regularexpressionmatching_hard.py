# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:


# input: string and pattern with . for any single character and * for zero or more of the preceding element -> output: bool of whether the pattern can match the string

# solve this problem dynamically with recursion?
# let's work through the examples
# if the pattern doesn't contain any . and doesn't have all the letters of the string, then we can immediately return false
# if the pattern doesn't contain any * and doesn't match the length of the string, we can immediately return false
# if the pattern does contain * and has all the letters of the string, then we can possibly return true
# if the pattern doesn't contain all the letters or the length of the string, but does contain . and * then we can possible return true

# how do we want to approach this?
# initially, traversing from left to right or right to left comes to mind.  Along the way, we could check if there's a match, and come up with conditions for an eager false return.
# recursion does seem to play really nicely then, why don't we come up with base case situations where we could either return true or false

# well, in our base case if string and pattern are empty, then we can return true
# if string is not empty and pattern is empty, then we can return false
# if string is empty but pattern is not empty, then we can return false
# if the next letter of pattern does not match the next letter of string, we can return false

# if there were no kleene stars (*), the problem would be easier - simply check from left to right if each character of the text matches the pattern
# when a star is present, we may need to check many different suffixes of the text and see if they match the rest of the pattern.  A recursive solution is a straightforward way to represent this.

# without kleene stars, our solution looks like this:

def match(text, pattern):
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])

# if a star is present in the pattern, it will be in the second position pattern[1].  Then, we may ignore this part of the pattern, or delete a matching character in the text.  If we have a match on the remaining strings after any of these operations, then the inital inputs matched.


class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

# Approach 2: Dynamic Programming
# Intuition


class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {
                        text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
