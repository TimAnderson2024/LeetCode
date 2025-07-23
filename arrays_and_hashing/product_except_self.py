from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        cur_prod = 1
        for i in range(1, len(nums)):
            cur_prod *= nums[i - 1]
            prefix[i] = cur_prod

        cur_prod = 1
        for i in range(len(nums) - 2, -1, -1):
            cur_prod *= nums[i + 1]
            suffix[i] = cur_prod

        ans = []
        for i in range(0, len(nums)):
            ans.append(prefix[i] * suffix[i])

        return ans
