from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = max(nums)
        prefix, suffix = 1, 1

        for i, num in enumerate(nums):
            prefix = prefix * num
            suffix = suffix * nums[-i - 1]
            cur_max = max(cur_max, prefix, suffix)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

        return cur_max
