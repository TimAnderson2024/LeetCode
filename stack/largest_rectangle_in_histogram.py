from typing import List


def largestRectangleArea(self, heights: List[int]) -> int:
    max_area = 0
    stack = []
    for i, height in enumerate(heights):
        left = i
        while stack and stack[-1][1] > height:
            prev_left, prev_height = stack.pop()
            area = (i - prev_left) * prev_height
            max_area = max(area, max_area)
            left = prev_left

        stack.append((left, height))
    for left, height in stack:
        area = (len(heights) - left) * height
        max_area = max(area, max_area)

    return max_area
