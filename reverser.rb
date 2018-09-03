# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
#
# Reverse String
#
# Write a function that takes a string as input and returns the string reversed.
#
# Example 1:
#
# Input: "hello"
# Output: "olleh"
# Example 2:
#
# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"

# @param {String} s
# @return {String}
def reverse_string(s)
    left = 0
    right = s.length - 1

    while left <= right
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1
    end

    return s
end
