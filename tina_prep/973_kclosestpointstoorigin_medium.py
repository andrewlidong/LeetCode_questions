# import heap
from heapq import *


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        kClosestPointsToOrigin = []

        # add first k points
        for i in range(K):
            heappush(kClosestPointsToOrigin,
                     (-Solution.getDistanceFromOrigin(points[i]), points[i]))

        # maintain k closest in heap for the remaining points
        for i in range(K, len(points)):
            heappushpop(kClosestPointsToOrigin,
                        (-Solution.getDistanceFromOrigin(points[i]), points[i]))

        # return each point in the heap
        return [heappop(kClosestPointsToOrigin)[1] for _ in range(K)]

    @staticmethod
    def getDistanceFromOrigin(point):
        return math.sqrt(point[0]**2 + point[1]**2)


# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         maxHeap = []
#         # put first k points in the max heap
#         for i in range(K):
#             heappush(maxHeap, points[i])

#         # go through remaining points of the input array, if a point is closer to the origin than the top point of the max-heap, remove the top point from the heap and add the point from the input array
#         for i in range(K, len(points)):
#             if points[i][0] **2 + points[i][1]**2 < maxHeap[0][0] **2 + maxHeap[0][1] **2:
#                 heappop(maxHeap)
#                 heappush(maxHeap, points[i])

#         # the heap has 'k' points closest to the origin, return them in a list
#         return list(maxHeap)

# Time: O(NlogK)
# Space: O(K)

# # import heap
# from heapq import *

# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         maxHeap = []
#         # put first k points in the max heap
#         for i in range(K):
#             heappush(maxHeap, self.distanceFromOrigin(points[i]))

#         # go through remaining points of the input array, if a point is closer to the origin than the top point of the max-heap, remove the top point from the heap and add the point from the input array
#         for i in range(K, len(points)):
#             if self.distanceFromOrigin(points[i]) < self.distanceFromOrigin(maxHeap[0]):
#                 heappop(maxHeap)
#                 heappush(maxHeap, points[i])

#         # the heap has 'k' points closest to the origin, return them in a list
#         return list(maxHeap)


#     def distanceFromOrigin(point: List[int]) -> i:
#         return point[0] **2 + point[1] **2

# Time: O(N * logK) since we're iterating all points and pushing them into the heap
# Space: O(K) because we need to store K points in the heap

# inputs: array of cartesian points (tuples or two-size arrays), integer of k closest points
# output: array of k cartesian points from input s.t. k points are all close to [0,0]

# to find distance from origin, return tuple[0] * tuple[0] + tuple[1] * tuple[1] (we can ignore square root to calculate the distance)

# put the first k points into a max heap
# go through the remaining points of the input array.  If a point is closer to the origin than the top point of the max-heap, remove the top point from the max heap and add the point from the input array
# the heap has k closest points to the origin, so return them in a list


# class Solution:
#     def kClosest(self, points, K):
#         points.sort(key= lambda P: P[0] ** 2 + P[1] ** 2)
#         return points[:K]

# Time: O(NlogN)
# Space: O(N)
