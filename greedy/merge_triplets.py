from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        has_appeared = [False, False, False]

        for triplet in triplets:
            is_valid = True
            for i, elem in enumerate(triplet):
                if elem > target[i]:
                    is_valid = False

            if not is_valid:
                continue

            for i, elem in enumerate(triplet):
                if elem == target[i]:
                    has_appeared[i] = True

        return all(has_appeared)
