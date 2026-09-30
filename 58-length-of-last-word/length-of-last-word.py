class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = 0

        current = 0
        for ch in s:
            if ch == ' ':
                current = 0
            else:
                current += 1
                longest = current
        
        return longest