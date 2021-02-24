class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # create dictionary for indices
        dic = {}
        new_words = []
        # populate dictionary with indices
        for i, ch in enumerate(order):
            dic[ch] = i
        # for each word, come up with a new word consisting of indices
        for w in words:
            new = []
            for c in w:
                new.append(dic[c])
            new_words.append(new)
        # comparing new words against everything else, see if the new word is out of order.
        for w1, w2 in zip(new_words, new_words[1:]):
            if w1 > w2:
                return False
        return True

# create a dictionary where the key is each word in new order, value is its index meaning its new position is in the new order
# transform the list of words into its index in new order.
# zip
# for list comparison, if we want w1 < w2, if len(w1) = len(w2) if will compare each element in w1/w2.

# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         indices = {c: i for i, c in enumerate(order)}
#         for a,b in zip(words, words[1:]):
#             if len(a) > len(b) and a[:leb(n)] == b:
#                 return False
#             for s1, s2 in zip(a, b):
#                 if indices[s1] < indices[s2]:
#                     break
#                 elif indices[s1] > indices[s2]:
#                     return False
#         return True

# # hash indices of each character for runtime
# # compare every adjcent word
# # if any letter or former word is in higher order, return False
# # if the current letter of former word is in lower order, forget the rest of the word
# # if the length of the former word is longer and the later word is a substring of the former, return False
# # return True
