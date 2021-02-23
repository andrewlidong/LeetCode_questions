# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # keep a dummy head for your return
        dummy = current = ListNode(0)
        # keep track of the remainder after the addition of the two
        remainder = 0

        while l1 or l2 or remainder:
            if l1:
                # add l1 to remainder
                remainder += l1.val
                # increment l1
                l1 = l1.next
            if l2:
                # essentially add l1 and l2 together
                remainder += l2.val
                # increment l2
                l2 = l2.next
            # write the next node of the return as the modulo of the remainder
            current.next = ListNode(remainder % 10)
            # increment current
            current = current.next
            # reduce size of remainder
            remainder //= 10
        return dummy.next

# Time: O(l1 + l2)
# Space: O(l1 + l2)

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         number1, number2, sumNumber, resultArray = 0, 0, 0, []
#         for idx1, i in enumerate(reversed(l1)):
#             if idx1 == 0:
#                 number1 += i
#             else:
#                 number1 += i * 10
#         for idx2, j in enumerate(reversed(l2)):
#             if idx2 == 0:
#                 number2 += j
#             else:
#                 number2 += j * 10
#         sumNumber = number1 + number2

#         while sumNumber > 0:
#             resultArray.append(sumNumber % 10)
#             sumNumber // 10

#         return resultArray


# pop numbers from the back of the list, multiply by 10, until the lists are empty.
# alternatively we could just iterate from the back of the list, that might be cleaner since we're not mutating the original arrays
# add them together
# Modulo by 10 and append that number to a new array.  Then floor divide by 10 until the new number is empty.
