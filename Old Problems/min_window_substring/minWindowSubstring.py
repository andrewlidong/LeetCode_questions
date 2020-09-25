class Solution(object):
    def minWindow(self, s, t):
        need = collections.defaultdict(int)
        for c in t: need[c] += 1

        missing = len(t)
        start_idx = lo = hi = 0

        def consume(char):
            nonlocal missing, need
            missing -= need[char] > 0
            need[char] -= 1

        def window_contains_t(): return not missing

        def move_start_to_the_right_as_possible():
            nonlocal need, start_idx
            while start_idx < end_idx and need[s[start_idx]] < 0:
                need[s[start_idx]] += 1
                start_idx += 1

        def update_range_if_smaller():
            nonlocal lo,hi
            if not hi or end_idx - start_idx <= hi - lo:
                lo, hi = start_idx, end_idx

        for end_idx, char in enumerate(s, 1):
            consume(char)

            if window_contains_t():
                move_start_to_the_right_as_possible()
                update_range_if_smaller()

        return s[lo:hi]
