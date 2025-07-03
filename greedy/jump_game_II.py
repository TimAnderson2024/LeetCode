from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_interval = 0
        left_bound = right_bound = 0

        # Iterate and create intervals until right_bound reaches end
        while right_bound < len(nums) - 1:
            # Find the farthest point we can jump from this interval
            # This will become the right_bound for the next interval
            max_jump = 0
            for i in range(left_bound, right_bound + 1):
                max_jump = max(i + nums[i], max_jump)
            # Setup next interval
            cur_interval += 1
            left_bound = right_bound + 1
            right_bound = max_jump

        return cur_interval
