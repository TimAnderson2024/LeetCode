from typing import List


def trap(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    maxLeft, maxRight = height[l], height[r]
    totalWater = 0

    while l < r:
        if maxLeft < maxRight:
            totalWater += maxLeft - height[l]
            l += 1
            maxLeft = max(maxLeft, height[l])
        else:
            totalWater += maxRight - height[r]
            r -= 1
            maxRight = max(maxRight, height[r])

    return totalWater
