from typing import List
import math


def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # Set up bounds for search space
    l, r = 1, max(piles)
    min_speed = 0

    while l <= r:
        cur_speed = (l + r) // 2

        # Calculate the time for this speed
        eat_time = 0
        for pile in piles:
            eat_time += math.ceil(pile / cur_speed)
        # Decrease speed if fast
        if eat_time <= h:
            min_speed = cur_speed
            r = cur_speed - 1
        # Increase speed if slow
        else:
            l = cur_speed + 1

    return min_speed
