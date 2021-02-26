class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0

            temp = n1 + n2 + carry
            res.append(temp % 10)
            carry = temp // 10
        if carry:
            res.append(carry)
        return ''.join([str(i) for i in res])[::-1]

# Input: num1 string, num2 string
# Output: num1 + num2

# figure out a way to translate a number string to a int so you can add them
# add each digit together

# Initialize an empty res structure.
# Start from carry = 0
# set a pointer at the end of each string: p1 = num1.length() - 1, p2 = num2.length() - 1
# loop over the strings from the end to the beginning using p1 and p2.  Stop when both strings are used entirely
# set x1 to be equal to a digit from string nums1 at index p1.  If p1 has reached the beginning of nums1, set x1 to 0.
# do the same for x2.  Set x2 to be equal to digit from string nums2 at index p2.  If p2 has reached the beginning of nums2, set x2 to 0.
# Compute the current value: value = (x1 + x2 + carry) % 10 and update the carry:
# carry = (x1 + x2 + carry) / 10
# Append the current value to the result: res.append(value)
# Now both strings are done.  If the carry is still non-zero, update the result: res.append(carry)
# Reverse the result, convert it to a string, and return that string.
