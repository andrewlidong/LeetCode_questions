class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(combination, next_digits):
            # if there are no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output

# Time: O(3^N * 4^M) where N is the number of digits in the input that map to 3 letters and M is the number of digits that map to.4 letters and N + M is the total number of digits in the input
# Space: O(3^N * 4^M) since one has to keep 3^N * 4^M solutions


# input: digits up to length 4 with range 2-9 -> output: array of string combinations of that digit
# create a hashmap of number keys to letter values.
# iterate through the digits of the string, and for each one, apply backtracking.
