# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        next = None

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

# Time: O(N)
# Space: O(1)


# Store previous, current, and next
# previous should be None, since it's technically what we now want our head to be pointing towards
# current can be just the head
# next can be None (in the case of a single ListNode this could be relevant)


# first save the next value (this will eventually be made our current)
# have current point to previous (for the first node this will be None, but later on it will be the current that we are trailing)
# set previous to current
# set current to the original next and continue moving down the LinkedList

# A great way to solve this problem is to draw it out and assign pointers yourself.
