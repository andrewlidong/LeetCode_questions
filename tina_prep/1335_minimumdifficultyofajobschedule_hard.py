class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        # class Solution:
        #     def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        #         job_count = len(jobDifficulty)
        #         # if there aren't enough jobs to work on at least one a day just default return -1
        #         if job_count < d: return -1

        #         def min_score(last_score=0, cur_idx=0, div_left=d-1):
        #             # our last day, we have to keep working until we're out of jobs
        #             if div_left == 0: return max([last_score] + jobDifficulty[cur_idx:])
        #             # our difficulty for today might increase since we take on this job
        #             cur_score = max(last_score, jobDifficulty[cur_idx])

        #             if job_count - cur_idx == div_left + 1:
        #                 # we have to keep splitting to have 1 job per day
        #                 return cur_score + sum(jobDifficulty[cur_idx + 1:])
        #             # keep working
        #             join_score = min_score(cur_score, cur_idx + 1, div_left)
        #             div_score = cur_score + min_score(0, cur_idx + 1, div_left - 1) # start fresh tomorrow
        #             return min(join_score, div_score)

        #         return min_score()
