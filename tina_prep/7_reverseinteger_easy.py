class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        while x:
            result = result * 10 + x % 10
            x //= 10

        return 0 if result > pow(2, 31) else result * sign

# Input: signed 32-bit integer x -> Outpu: signed input 32-bit integer with digits reversed.  If its outside the 32-bit integer range, return 0.

# build the reverse integer one digit at a time.  Check beforehand whether or not appending another digit would cause an overflow
# reversing an integer can be done similarly to reversing a string
# we want to repeatedly pop the last digit off of x and push it to the back of the rev.  In the end, rev will be the reverse of the x.
