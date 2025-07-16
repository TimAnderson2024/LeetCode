class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for i, char in enumerate(s):
            if i > 0 and s[i - 1] == char:
                left_even = self.find_radius(s, i - 1, i)
                max_palindrome = (
                    left_even
                    if len(left_even) > len(max_palindrome)
                    else max_palindrome
                )
            if i < len(s) - 1 and s[i + 1] == char:
                right_even = self.find_radius(s, i, i + 1)
                max_palindrome = (
                    right_even
                    if len(right_even) > len(max_palindrome)
                    else max_palindrome
                )
            odd = self.find_radius(s, i, i)
            max_palindrome = odd if len(odd) > len(max_palindrome) else max_palindrome
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
