from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    sums = []

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            cur_sum = num + nums[l] + nums[r]
            if cur_sum > 0:
                r -= 1
            elif cur_sum < 0:
                l += 1
            else:
                sums.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return sums
