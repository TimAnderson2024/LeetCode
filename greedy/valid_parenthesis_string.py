class Solution:
    def checkValidString(self, s: str) -> bool:
        left_paren = []
        wild_card = []

        for i, char in enumerate(s):
            if char == "(":
                left_paren.append(i)
            elif char == "*":
                wild_card.append(i)
            else:
                if left_paren:
                    left_paren.pop()
                elif wild_card:
                    wild_card.pop()
                else:
                    return False

        while left_paren and wild_card:
            if wild_card[-1] > left_paren[-1]:
                wild_card.pop()
                left_paren.pop()
            else:
                return False

        return len(left_paren) == 0
