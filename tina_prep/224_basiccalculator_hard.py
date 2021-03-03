# class Solution:
#     def calculate(self, s: str) -> int:


# Input: a string representing an expression (with +,-,(,) and ' ') -> Output: integer evaluating it

# we need to handle +, -, parens and spaces, which we can basically ignore.
# I think, when we run into an open parens, we should probably recursively invoke calculate
# I think calculate should handle plus and minus, and ignore spaces
# I think we should have a way of converting string to ints,
# we need to figure out the full length of an int before converting it to string.  We can temporarily store it in another string?  That makes sense.

# iterate from left to right of the string
# if it's a space, skip it.
# if it's a string from 0-9, store it

# not completed in 15 minutes.

# Solution:

# Input always contains strings
# Rules of addition and subtraction
# Implication of precedence by parenthesis
# Spaces do not affect the evaluation of the input expression.

# 1: Stack and String Reversal
# We could reverse the string and then use basic drill using a stack.  Reversing a string helps since we put the elements of the expression into the stack from right to left and evaluation is done correctly from left to right.
# Algorithm:
# 1. Iterate the expression string in reverse order one character at a time.  Since we are reading the expression character by character, we need to be careful when we are reading digits and non-digits.
# 2. The operands could be formed by multiple characters.  If the character read is a digit we need to form the operand by multiplying a power of 10 to the current digit and additng it to the overall operand.  We do this since we are processing the string in the reverse order.
# 3. The operands could be formed by multiple characters.  We need to keep track of an ongoing operand.
# 4. When we encounter an opening parenthesis (, this means an expression just ended (remember, we reversed the expression).  So an opening bracket signifies the end of an expression.  This calls for evaluation of the expression by popping operands and operators off the stack till we pop corresponding closing parenthesis.
# 5. Push the other non-digits onto the stack
# 6. Do this until we get the final result.  Once we are done evaluating the entire expression, check if the stack is non-empty.  If so, we treat the elements in it as one final expression and evaluate the same way we would if we had encountered an opening bracket.

# class Solution:

#     def evaluate_expr(self, stack):

#         res = stack.pop() if stack else 0

#         # Evaluate the expression till we get corresponding ')'
#         while stack and stack[-1] != ')':
#             sign = stack.pop()
#             if sign == '+':
#                 res += stack.pop()
#             else:
#                 res -= stack.pop()
#         return res

#     def calculate(self, s: str) -> int:

#         stack = []
#         n, operand = 0, 0

#         for i in range(len(s) - 1, -1, -1):
#             ch = s[i]

#             if ch.isdigit():

#                 # Forming the operand - in reverse order.
#                 operand = (10**n * int(ch)) + operand
#                 n += 1

#             elif ch != " ":
#                 if n:
#                     # Save the operand on the stack
#                     # As we encounter some non-digit.
#                     stack.append(operand)
#                     n, operand = 0, 0

#                 if ch == '(':
#                     res = self.evaluate_expr(stack)
#                     stack.pop()

#                     # Append the evaluated result to the stack.
#                     # This result could be of a sub-expression within the parenthesis.
#                     stack.append(res)

#                 # For other non-digits just push onto the stack.
#                 else:
#                     stack.append(ch)

#         # Push the last operand to stack, if any.
#         if n:
#             stack.append(operand)

#         # Evaluate any left overs in the stack.
#         return self.evaluate_expr(stack)

# Time: O(N) where N is the length of the string
# Space: O(N) where N is the length of the string

# Approach 2: Stack and No String Reversal

# One way we can get around the challenge of subtraction is to just treat elements after it as negative versions of themselves.
# Keep in mind that expressions given would be complicated ( there would be lots of nesting), so we need to associate the negative sign outside of B-C with the result of B-C instead of just with B
# Solve this problem by associating the sign with the expression to the right of it.  However, we can reduce push and pop operations by evaluating most of the expressions on the go.

# Algorithm
# 1. Iterate the expression string one character at a time.  Since we are reading the expression character by character, be careful when we're reading digits and non-digits.
# 2. The operands could be formed by multiple characters.  A string '123' would mean a numeric 123, which could be formed in many ways.  If the character read is a digit we need to form the operand by multiplying 10 to the previously formed continuing operand and adding the digit to it.
# 3. Whenever we encounter an operator such as + or - we first evaluate the expression to the left and then save this sign for the next evaluation.
# 4. If the character is an opening parenthesis, just push the result calculated so far and the sign on to the stack (the sign and the magnitude) and start fresh as if we are calculating a new expression.
# 5. If the character is a closing parenthesis, we first calculate the expression to the left.  The result would be the expression within the set of parenthesis that just concluded.
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0  # For the on-going result
        sign = 1  # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop()  # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop()  # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand

# Time Complexity: O(N), where N is the length of the string.
# Space Complexity: O(N), where N is the length of the string
