
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:

from Queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         minHeap = []

#         # put the root of each list in the min heap
#         for root in lists:
#             if root is not None:
#                 heappush(minHeap, root)

#         # take the smallest(top) element from the min-heap and add it to the result
#         # if the top element has a next element add it to the heap
#         resultHead, resultTail = None, None
#         while minHeap:
#             node = heappop(minHeap)
#             if resultHead is None:
#                 resultHead = resultTail = node
#             else:
#                 resultTail.next = node
#                 resultTail = resultTail.next

#             if node.next is not None:
#                 heappush(minHeap, node.next)

#         return resultHead


# If we have to find the smallest element of all the input lists, we have to compare only the smallest (first) element of all the lists.  Once we have the smallest element, we can put it in the merged list.  Following a similar pattern, we can then find the next smallest element of all the lists to add it to the merged list.

# The best data structure that comes to mind is a Heap.

# Insert the first element of each array in a Min Heap.
# After this, we can take out the smallest(top) element from the heap and add it to the merged list.
# After removing the smallest element from the heap, we can insert the next element of the same list into the heap.
# We can repeat steps 2 and 3 to populate the merged list in sorted order.

# Compare one by one
# Compare every k nodes (head of every linked list) and get the node with the smallest value
# Extend the final sorted linked list with the selected nodes

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         self.nodes = []
#         head = point = ListNode(0)
#         for l in lists:
#             while l:
#                 self.nodes.append(l.val)
#                 l = l.next
#         for x in sorted(self.nodes):
#             point.next = ListNode(x)
#             point = point.next
#         return head.next

# Time Complexity: O(NlogN) where N is the total number of nodes
# Collecting all the values costs O(N) time
# A stable sorting algorithm costs O(NlogN) time
# Iterating for creating the linked list costs O(N) time

# Space Complexity: O(N)
# Sorting cost O(N) space (depends on the algorithm you choose)
# Creating a new linked list costs O(N) space


# Inputs and Outputs

# Input: array of k linked-lists, each linked-list sorted in ascending order -> Output: merge all linked-lists into one sorted linked-list and return it.

# Brute force algorithm would be to traverse all linked lists and collect the values of the nodes into an array.  Then sort and iterate over this array to get the proper value of nodes, then create a new sorted linked list and extend it with the new nodes.
