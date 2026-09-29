class Solution:
    def maxPower(self, s: str) -> int:
        longest = 1
        current = 1

        current_char = ''
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current += 1

                longest = max(longest, current)
            else:
                current = 1

        return longest 