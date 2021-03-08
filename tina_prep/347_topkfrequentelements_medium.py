from heapq import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # find the frequency of each number
        numFrequencyMap = {}
        for num in nums:
            numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1

        minHeap = []

        # go through all numbers of the numFrequencyMap and push them in the minHeap, which will have the top k frequent numbers.  If the heap size is more than k, we remove the smallest(top) number
        for num, frequency in numFrequencyMap.items():
            heappush(minHeap, (frequency, num))
            if len(minHeap) > k:
                heappop(minHeap)

        # create a list of top k numbers
        topNumbers = []
        while minHeap:
            topNumbers.append(heappop(minHeap)[1])

        return topNumbers


# input: non-empty array of integers -> output: k most frequent elements

# Solution: use a Hashmap to keep track of the frequency of each number, then use a Min Heap to find the K most frequently occuring numbers.  In the min heap, instead of comparing numbers, compare their frequencies in order to get frequently occurring numbers.
