from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Count occurances
        count = Counter(hand)

        # Iterate over each card
        for card in hand:
            # Look backwards until we find the start of a straight
            start_card = card
            while count[start_card - 1]:
                start_card = start_card - 1

            # Attempt to form group
            while start_card <= card:
                while count[start_card]:
                    for next_card in range(start_card, start_card + groupSize):
                        if not count[next_card]:
                            return False
                        count[next_card] -= 1
                start_card += 1

        return True
