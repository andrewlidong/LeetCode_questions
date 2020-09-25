# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# Example :
#
# Input: n = 10, pick = 6
# Output: 6

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left = 0
        right = n
        while left <= right:
            num = (left + right) / 2
            result = guess(num)
            if result == 0:
                return num
            elif result == 1:
                left = num + 1
            else:
                right = num - 1
