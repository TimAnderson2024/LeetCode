class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for i, char in enumerate(s):
            # Test for even-length palindrome
            if i < len(s) - 1 and s[i + 1] == char:
                even = self.find_radius(s, i, i + 1)
                if len(even) > len(max_palindrome):
                    max_palindrome = even
            # Test for odd-length palindrome
            odd = self.find_radius(s, i, i)
            if len(odd) > len(max_palindrome):
                max_palindrome = odd
        return max_palindrome

    def find_radius(self, s, center_lb, center_rb):
        radius = 0
        while (
            center_lb - (radius + 1) >= 0
            and center_rb + (radius + 1) < len(s)
            and s[center_lb - (radius + 1)] == s[center_rb + (radius + 1)]
        ):
            radius += 1

        return s[center_lb - radius : center_rb + radius + 1]
