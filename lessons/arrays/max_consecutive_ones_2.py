class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        i = 0
        res = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                cnt += 1
            while j - i + 1 - cnt > 1:
                if nums[i] == 1:
                    cnt -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
