def isPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not is_alphanumeric(s[l]):
            l += 1
        while l < r and not is_alphanumeric(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


def is_alphanumeric(char) -> bool:
    return ("0" <= char <= "9") or ("a" <= char <= "z") or ("A" <= char <= "Z")
