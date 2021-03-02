class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        A = self.M.get(key, None)
        if A is None:
            return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""

# Time: O(1) for each set operation and O(logN) for each get operation, where N is the number of entries in the TimeMap.

# Space Complexiy: O(N)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# set: input: key, value, timestamp -> output: None
# get: input: key, timestamo -> output: value

# all k/v strings are lowercase
# all k/v strings have length [1,100]
# timestamps for all TimeMap.set operations are strictly increasing
# set and get will be called a lot of times.

# class TimeMap(object):
#     def __init__(self):
#         self.dic = collections.defaultdict(list)

#     def set(self, key, value, timestamp):
#         self.dic[key].append([timestamp, value])

#     def get(self, key, timestamp):
#         arr = self.dic[key]
#         n = len(arr)

#         left = 0
#         right = n

#         while left < right:
#             mid = (left + right) / 2
#             if arr[mid][0] <= timestamp:
#                 left =mid + 1
#             elif arr[mid][0] > timestamp:
#                 right = mid

#         return "" if right == 0 else arr[right - 1][1]
