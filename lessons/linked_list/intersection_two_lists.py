class Solution:
    def getSize(self, head: ListNode) -> int:
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next

        return size

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        size_of_a, size_of_b = self.getSize(headA), self.getSize(headB)

        diff = size_of_a - size_of_b

        # length alignment
        if diff > 0:
            for i in range(diff):
                headA = headA.next

        elif diff < 0:
            for i in range(abs(diff)):
                headB = headB.next

        # start traversal after length alignment
        # A and B will meet at either intersection or NULL on tail
        while headA and headB:
            if headA is headB:
                break

            headA = headA.next
            headB = headB.next
        return headA


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_a, cur_b = headA, headB

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB
            cur_b = cur_b.next if cur_b else headA

        return cur_a
