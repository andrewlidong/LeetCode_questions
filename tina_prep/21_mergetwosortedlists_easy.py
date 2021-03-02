# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        merged = head
        while l1 and l2:
            if l1.val <= l2.val:
                merged.next = l1
                merged = merged.next
                l1 = l1.next
            elif l1.val > l2.val:
                merged.next = l2
                merged = merged.next
                l2 = l2.next

        if l1:
            merged.next = l1
            merged = merged.next
            l1 = l1.next

        if l2:
            merged.next = l2
            merged = merged.next
            l2 = l2.next

        return head.next

# Time: O(N + M)
# Space: O(N + M)


# input: l1 listNode head, l2 listNode head -> output: list[array]

# initialize an empty array for return
# while l1 and l2, compare the two heads, and append the value of the smaller one.
# once we run into the end of l1 or l2 (we'll have a next value of none)
# we can then push the remainder of whatever l1 or l2 into the mergedTwoLists
# return the mergedLists

# # nice recursive solution

# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         if l1 is None:
#             return l2
#         elif l2 is None:
#             return l1
#         elif l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2

# # Time: O(N + M)
# # Space: O(N + M)

# # iterative solution

# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         # maintain an unchanging reference to node ahead of the return node.
#         prehead = ListNode(-1)

#         prev = prehead
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 prev.next = l1
#                 l1 = l1.next
#             else:
#                 prev.next = l2
#                 l2 = l2.next
#             prev = prev.next

#         # at least one of l1 and l2 can still have nodes at this point, so connect the non-null list to the end of the end of the merged list
#         prev.next = l1 if l1 is not None else l2

#         return prehead.next
