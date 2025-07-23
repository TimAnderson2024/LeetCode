from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r, row in enumerate(board):
            for c, char in enumerate(row):
                if board[r][c] != ".":
                    if (
                        (char in rows[r])
                        or (char in cols[c])
                        or (char in squares[(r // 3, c // 3)])
                    ):
                        return False
                    rows[r].add(char)
                    cols[c].add(char)
                    squares[(r // 3, c // 3)].add(char)
        return True
