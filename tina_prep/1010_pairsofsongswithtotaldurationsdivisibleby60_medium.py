# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         pairs = []
#         for i in range(len(time) - 1):
#             for j in range(i + 1, len(time)):
#                 if (time[i] + time[j]) % 60 == 0:
#                     pairs.append([i,j])
#         return len(pairs)

# Time Complexity: O(N^2), exceeded time limit
# Space Complexity: O(1)

# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         pairs = []
#         potentialMatch = {}
#         for i, num in enumerate(time):
#             if num % 60 in potentialMatch:
#                 pairs.append([potentialMatch[num%60], i])
#             potentialMatch[num] = i

#         return len(pairs)


# ith song has a duration of time[i] seconds
# we want i, j in List[int] s.t. i < j and time[i] + time[j] % 60 == 0, but just the number of times.

# brute force we can iterate through each index and then check the remainder to see whether the two together are divisible by 60.  This will be n^2
# we can't quite use the hash trick from twosum.  I suppose we could if we stored index position actually.
# we can't even really use the two pointer trick because we don't know that the list is sorted, and index position really matters to us

# Solution:

# Approach 1: Brute Force
# Iterate through the entire array using a nested loop to examine that, for each element a in time, whether there is another element b such that (a + b) % 60 == 0.  This is probably too brutal to pass an interview

# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         ret, n = 0, len(time)
#         for i in range(n):
#             # j starts with i + 1 so that i is always to the left of j to avoid repetitive counting
#             for j in range(i + 1, n):
#                 ret += (time[i] + time[j]) % 60 == 0
#         return ret


# Approach 2: Use an Array to Store Frequencies
# Iterate through the input array time, and for each element a, we want to know the number of elements b such that:
# 1. b % 60 = 0 if a % 60 = 0
# 2. b % 60 = 60 - a % 60 if a % 60 != 0

# Implement this logic by repeatedly examining the rest of time again and again for each element a.  However, we are able to improve by consuming more space - we can store the frequencies of the remainder of complements in O(1) time.

# Initiate an array remainders with size 60 to record the frequencies of each remainder - as the range of remainders is [0, 59].  Then we can loop through the array once and for each element a we would check if:
# a % 60 == 0, add remainders[0] to the result, else add remainders[60 - t % 60] to the result
# update remainders [a % 60]

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0:  # check if a % 60 == 0 && b % 60 == 0
                ret += remainders[0]
            else:  # check if a % 60 + b % 60 == 60
                ret += remainders[60 - t % 60]
            remainders[t % 60] += 1  # remember to update the remainders
        return ret

# time complexity: O(n) where n is the length of the input array because we visit each element in time once
# space complexity: O(1) because the size of the array is fixed with 60.
