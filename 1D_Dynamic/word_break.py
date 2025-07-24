from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def build_word(cur_word):
            if cur_word in cache:
                return cache[cur_word]
            if cur_word == s:
                return True

            for word in wordDict:
                if (
                    len(cur_word) + len(word) <= len(s)
                    and word == s[len(cur_word) : len(cur_word) + len(word)]
                ):
                    if build_word(cur_word + word):
                        cache[cur_word] = True
                        return True

            cache[cur_word] = False
            return False

        return build_word("")
