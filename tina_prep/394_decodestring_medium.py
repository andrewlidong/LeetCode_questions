class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentNumber = 0
        currentString = ''
        for c in s:
            if c == '[':
                stack.append(currentString)
                stack.append(currentNumber)
                currentString = ''
                currentNumber = 0
            elif c == ']':
                num = stack.pop()
                previousString = stack.pop()
                currentString = previousString + num * currentString
            elif c.isdigit():
                currentNumber = currentNumber * 10 + int(c)
            else:
                currentString += c
        return currentString

# Input: encoded string with some numbers, brackets and letters -> Output: decoded string with just letters
# Initially, we need a function that sees a number, and knows to immediately look for the brackets, and then repeats that bracketed letter number amount of times.
# We can probably just iterate from left to right of the encoded string and feed into the decoded string character by character.
# So, if it's just a character, just feed it into the decoded string.
# If we get a number, we want to keep track of that number (and eventually decrement it every time we feed the decoded string the interior)
# We also have to figure out how far the queue or stack goes, so we'll probably memoize the interior, and cut off once we have the end bracket.  Recursion seems like a fine way to go about this.

# Approach 1: Using Stack

# Intution
# We have to decode the result in a particular pattern.  We know that the input is always valid.  The pattern begins with a number k, followed by opening braces [, followed by string.  Post that, there could be one of the following cases:

# 1. There is another nested pattern k[string k[string]]
# 2. There is a closing bracket k[string]

# Since we have to start decoding the innermost pattern first, continue iterating over the string
