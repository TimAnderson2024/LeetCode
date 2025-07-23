from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}

        for num in nums:
            if num not in dups:
                dups[num] = 1
            else:
                return True
        return False
