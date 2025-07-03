from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If net gas is negative, route is impossible
        net_gas = sum(gas) - sum(cost)
        if net_gas < 0:
            return -1

        # Find first station where trip is positive
        start = 0
        cur_trip_cost = 0
        for i in range(len(gas)):
            cur_trip_cost += gas[i] - cost[i]
            if cur_trip_cost < 0:
                start = i + 1
                cur_trip_cost = 0

        return start
