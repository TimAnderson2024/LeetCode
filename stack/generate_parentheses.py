from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur_paren = []
        valid_paren = []

        def generate(num_open, num_closed):
            if num_open == num_closed == n:
                valid_paren.append("".join(cur_paren))
                return

            if num_open < n:
                cur_paren.append("(")
                generate(num_open + 1, num_closed)
                cur_paren.pop()
            if num_closed < num_open and num_closed < n:
                cur_paren.append(")")
                generate(num_open, num_closed + 1)
                cur_paren.pop()

        generate(0, 0)
        return valid_paren
