from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        max_len = 0
        for num in hashmap.keys():
            if num - 1 in hashmap:
                continue

            cur_len = 1
            while num + 1 in hashmap:
                cur_len += 1
                num += 1
            max_len = max(max_len, cur_len)
        return max_len
