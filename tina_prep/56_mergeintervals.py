class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        mergedIntervals = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current interval doesn't overlap with the previous, append it
            if not mergedIntervals or mergedIntervals[-1][1] < interval[0]:
                mergedIntervals.append(interval)
            else:
                # if there is an overlap, merge the current and previous
                mergedIntervals[-1][1] = max(mergedIntervals[-1]
                                             [1], interval[1])

        return mergedIntervals

# Time Complexity: O(N) where N is the number of intervals
# Space Complexity: O(N) since we need to create a new return array

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         mergedIntervals = []
#         currentInterval = intervals[0]
#         for idx in range(1, len(intervals))
#             if currentInterval[1] >= intervals[idx][0]:
#                 currentInterval[1] = intervals[idx][1]
#             else:
#                 mergedIntervals.append(currentInterval)
#                 currentInterval = intervals[idx]
#         return mergedIntervals


# iterate through each interval
# for each interval, check if the end is overlapping with the next interval.
# If two intervals are overalpping, merge them
# If two intervals are not overlapping, add the interval to your return array and move on
