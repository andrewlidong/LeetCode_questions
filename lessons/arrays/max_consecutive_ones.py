class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                # increment the count of 1's by one
                count += 1
            else:
                # find the maximum till now
                max_count = max(max_count, count)
                # reset count of 1
                count = 0
        return max(max_count, count)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, "".join(map(str, nums)).split('0')))