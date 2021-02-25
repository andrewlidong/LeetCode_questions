class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there is no meeting to schedule then no room needs to be allocated
        if not intervals:
            return 0

        # heap initialization
        free_rooms = []

        # sort meetings in ascending order based on their start time
        intervals.sort(key=lambda x: x[0])

        # add the first meeting.  We have to give a new room to the first meeting
        heapq.heappush(free_rooms, intervals[0][1])

        # for all the remaining meeting rooms
        for i in intervals[1:]:

            # if the room due to free up the earliest is free, assign that room to this meeting
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # if a new room is to be assigned, then also we add to the heap
            # if an old room is allocated, then we also add to the heap with updated end time
            heapq.heappush(free_rooms, i[1])

        # the size of the heap tells us the minimum rooms required for all the meetings
        return len(free_rooms)

# Time: O(NlogN)
# Sorting takes O(NlogN) considering the array consists of N elements
# min-heap, in the worst case all N meetings will collide with each other.  In any case we have N add operations on the heap.  In the worst case we will have N extract-min operations as well.  Overall complexity being NlogN since extract-min operation on a heap takes O(logN)

# Space: O(N) because we construct the min-heap and that can contain N elements in the worst case.


# input: array of intervals (which are themselves tuples or 2-sized arrays)
# output: integer of meeting rooms

# This question boils down to identifying how many overlapping intervals exist
# we can sort the intervals based on start time.
# naively we can check if a room is available or not by iterating on all the rooms and seeing if one is available when we have a new meeting at hand.
# we can do better than this by making use of priority queues or min-heap data structure
# we can keep all rooms in a min heap where the key for the min heap would be the ending time of a meeting
# every time we want to check if any room is free or not, simply check the topmost element of the min heap.

# Algorithm:
# Sort the given meetings by their start time
# initialize a new min-heap and add the first meeting's ending time to the heap.  We simply need to keep track of the ending times as that tells us when a meeting room will get free.
# for every meeting room check if the minimum element of the heap (the room at the top of the heap is free or not)
# if the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing
# if not, allocate a new room and add it to the heap
# after processing the meetings, the size of the heap will tell us the number of rooms allocated.  This wil be the minimum number of rooms needed to accomodate all the meetings.
