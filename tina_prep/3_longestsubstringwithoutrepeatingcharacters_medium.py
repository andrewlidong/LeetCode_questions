class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        window_start = 0
        max_length = 0

        for window_end in range(len(s)):
            right = s[window_end]
            if right not in chars:
                chars[right] = 0
            chars[right] += 1

            while chars[right] > 1:
                left = s[window_start]
                chars[left] -= 1
                if chars[left] == 0:
                    del chars[left]
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length

# time: O(N) where N is the size of the string
# space: O(1) since although we could hypothetically have a string of entirely distinct letters, that string will still be bounded by the size of the input (in the english language that's 26 characters)

# create a hash to keep track of characters and how often they come up
# use the sliding window approach - create a window_start and keep track of max_length
# iterate through the indices of the string.
# if a character is not in the hash, put it in and increment it's value by one.  If the number of characters' value is greater than 1, decrement it and delete it if it ever reaches 0.  Increment the window_start position.
# constantly update the max_length to be the max of the previous max_length and the current window size, keeping in mind to add 1 to the window_size for inclusivity.
# finally return the max_length
