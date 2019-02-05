# 406. Queue Reconstruction by Height

# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.


# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# SOLUTION: 

# First sort the list of people, in the order of decreasing height.  If multiple people are of the same height, sort them in ascending order of the number of people in front of them.  Then, for each person [i,j], their index in people_sorted is larger than or equal to j (due to the way we sort people).  Hence to obtain the final results, we just need to construct an empty list res, and starting from the left, insert each element [i,j] in people_sorted to position j in res (Latter insertions of [i', j'] won't affect j because eitehr i' < i or i' == i and j' > j).  

# The time complexity of the algorithm is O(n^2).  We loop over people once, and each insertion is an O(n) operation.  The space complexity is O(n).  

class Solution(object):
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res