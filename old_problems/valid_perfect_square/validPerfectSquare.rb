# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Output: true
# Example 2:
#
# Input: 14
# Output: false

def is_perfect_square(num)
  left = 0
  right = (num/2.0).ceil

  while left <= right
    mid = (left + right) / 2
    square = mid * mid
    if square == num
      return true
    elsif square < num
      left = mid + 1
    else
      right = mid - 1
    end
  end

  false
end
