class Solution:
    def climbStairs(self, n: int) -> int:
        step_a = 1
        step_b = 1

        for i in range(0, n):
            temp = step_b
            step_b = step_a + step_b
            step_a = temp

        return step_a
