from typing import List


# Complement version
def twoSumComplement(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    while l < r:
        complement = target - numbers[l]
        while numbers[r] > complement:
            r -= 1

        if numbers[r] == complement:
            return [l + 1, r + 1]

        l += 1


# True two pointer
def twoSumPointer(self, numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    while l < r:
        cur_sum = numbers[l] + numbers[r]

        if cur_sum == target:
            return [l + 1, r + 1]
        elif cur_sum > target:
            r -= 1
        else:
            l += 1

    return [l + 1, r + 1]
