# def oddEvenList(self, head):
#     dummy1 = odd = ListNode(0)
#     dummy2 = even = ListNode(0)
#     while head:
#         odd.next = head
#         even.next = head.next
#         odd = odd.next
#         even = even.next
#         head = head.next.next if even else None
#     odd.next = dummy2.next
#     return dummy1.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = ListNode(0)
        evens = ListNode(0)
        oddsHead = odds
        evensHead = evens
        isOdd = True
        while head:
            if isOdd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            isOdd = not isOdd
            head = head.next
        evens.next = None
        odds.next = evensHead.next
        return oddsHead.next
