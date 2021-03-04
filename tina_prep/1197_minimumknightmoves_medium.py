from functools import lru_cache


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None)
        def DP(x, y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            return min(DP(abs(x-1), abs(y-2)), DP(abs(x-2), abs(y-1)))+1
        return DP(abs(x), abs(y))
