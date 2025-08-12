from typing import List


def maxArea(heights: List[int]) -> int:
    l = 0
    r = len(heights) - 1
    maxArea = 0

    while l < r:
        curArea = min(heights[l], heights[r]) * (r - l)
        maxArea = max(curArea, maxArea)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return maxArea
