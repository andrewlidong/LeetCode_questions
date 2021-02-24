class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    result = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    result = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return result

# Time: O(N^2)
# Space: O(N)

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def helper(left, right):
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left + 1:right]

#         result = ""
#         for i in range(len(s)):
#             test = helper(i, i)
#             if len(test) > len(result): result = test
#             test = helper(i,i + 1)
#             if len(test) > len(result): result = test

#         return result

# create a helper function to check if a function is a palindrome
# palindrome checker goes from both

# helper to find middle
