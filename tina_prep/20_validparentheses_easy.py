class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary of key closed characters corresponding to value open characters
        parensDictionary = {'}': '{', ')': '(', ']': '['}
        parensStack = []

        for character in s:
            if character in parensDictionary.values():
                parensStack.append(character)
            elif character in parensDictionary.keys():
                if parensStack == [] or parensDictionary[character] != parensStack.pop():
                    return False
            else:
                return False
        return parensStack == []


# Create a dictionary of closed characters corresponding to open characters.
# Iterate through the string, and each time we run into an open character, put it into a stack.
# If at the end of our iteration we still have characters in our stack, then we return false
# If at the end of our iteration we don't have characters in our stack, then we return true.
