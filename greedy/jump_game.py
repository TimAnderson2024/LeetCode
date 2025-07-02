from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for pos in range(len(nums) - 1, -1, -1):
            if nums[pos] >= goal - pos:
                goal = pos

        return goal == 0
