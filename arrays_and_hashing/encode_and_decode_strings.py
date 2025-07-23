from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        code = ""
        for string in strs:
            code += str(len(string)) + "#" + string
        print(code)
        return code

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            num_char = ""
            while s[i] != "#":
                num_char += s[i]
                i += 1
            i += 1
            num_char = int(num_char)
            words.append(s[i : i + num_char])
            i = i + num_char

        return words
