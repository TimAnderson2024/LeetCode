from collections import Counter
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        seen = {}
        partitions = []
        cur_partition = 0

        for i, elem in enumerate(s):
            seen[elem] = seen.get(elem, 0) + 1
            cur_partition += 1

            if seen[elem] == count[elem]:
                del seen[elem]

            if not seen:
                partitions.append(cur_partition)
                cur_partition = 0

        return partitions
