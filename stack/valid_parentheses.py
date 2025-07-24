class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        lookup = {"{": "}", "[": "]", "(": ")"}
        for char in s:
            if char in "{[(":
                stk.append(char)
            else:
                if not stk or lookup[stk.pop()] != char:
                    return False

        return len(stk) == 0
