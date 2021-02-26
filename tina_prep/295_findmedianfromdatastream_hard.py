from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

        return -self.maxHeap[0] / 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# addNum input: int # output: just put it into a min or max heap depending on whichever one is smaller

# findmedian input: none, output: return the median of all elements so far

# store a minHeap and a maxHeap
# default by inserting into the maxHeap.  But make sure minHeap and maxHeap are balanced and only ever offset by 1 element in terms of size.
# if the maxHeap is greater than the minHeap, push into the minHeap and pop off the maxHeap
# if the maxHeap is smaller than the minHeap, push onto the maxHeap and pop off the minHeap
# essentially we're storing the largest number of half the elements and the smallest number of the other half
# when we want to find the median, if the heaps are the same length (if we have an even number of elements), return the two middle numbers divided by two.
# otherwise, return the maxHeap element since it's the middle element based on how wev'e set this all up

# time: O(logn) insertion since we're adding into a heap
# space: O(n) because we're storing all the numbers
