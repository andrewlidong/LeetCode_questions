class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        dic = collections.Counter(heights)

        start = 1
        ans = 0
        i = 0

        while i < len(heights):
            freq = dic[start]
            j = 0
            while j < freq:
                if heights[i] != start:
                    ans += 1
                j += 1
                i += 1
            start += 1

        return ans
