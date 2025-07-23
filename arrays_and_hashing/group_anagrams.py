from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            char_arr = [0] * 26
            for char in word:
                char_arr[ord(char) - ord("a")] += 1

            hashmap[tuple(char_arr)].append(word)

        return list(hashmap.values())
