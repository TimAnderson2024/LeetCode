class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}

        def calcWays(i: int):
            if i in cache:
                return cache[i]
            elif s[i] == "0":
                return 0

            numCodes = calcWays(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")
            ):
                numCodes += calcWays(i + 2)
            cache[i] = numCodes
            return numCodes

        return calcWays(0)
