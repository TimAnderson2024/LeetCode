from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = nums[0], nums[0]

        for num in nums[1:]:
            # Cut off prefix if negative
            if cur_sum < 0:
                cur_sum = 0

            # Add next element
            cur_sum += num
            max_sum = max(cur_sum, max_sum)

        return max_sum
