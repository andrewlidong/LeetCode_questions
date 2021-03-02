class Solution:
    def compress(self, chars: List[str]) -> int:
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1: left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left

# Time: O(N)
# Space: O(N)

# Input: array of characters -> Output: length of compressed string array

# create a return array
# Sort the character array
# count through the characters and put it into a return array, count the current number of repetitions, and when the letter switches, put it in and reset the number of repetitions.
# join the array characters and return it

# group the array into repeated chunks, keeping track of the character and the count.  This forms the encoded contents.
# update the original array with the encoded contents.  We maintain a left pointer to know which position to update the original array with the encoded contents and increment it according to the length of the encoded contents.
# the encoded contents will definitely be shorter than the original, so we can overwrite the original without worries.
