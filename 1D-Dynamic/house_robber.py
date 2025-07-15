from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        house_a, house_b = 0, 0

        for house in nums:
            cur_max = max(house + house_a, house_b)
            house_a = house_b
            house_b = cur_max

        return house_b
