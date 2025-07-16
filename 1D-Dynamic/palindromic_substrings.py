class Solution:
    def countSubstrings(self, s: str) -> int:
        num_palindromes = 0
        for i, char in enumerate(s):
            # Test for even-length palindromes
            if i < len(s) - 1 and s[i + 1] == char:
                num_palindromes += self.find_radius(s, i, i + 1)
            # Test for odd-length palindromes
            num_palindromes += self.find_radius(s, i, i)
        return num_palindromes

    def find_radius(self, s, center_lb, center_rb):
        radius = 0
        while (
            center_lb - (radius + 1) >= 0
            and center_rb + (radius + 1) < len(s)
            and s[center_lb - (radius + 1)] == s[center_rb + (radius + 1)]
        ):
            radius += 1

        return radius + 1
