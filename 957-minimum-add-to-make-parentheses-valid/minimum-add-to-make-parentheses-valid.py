class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        close_count = 0

        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    close_count += 1
            
            print(open_count, close_count)
        
        return abs(open_count+close_count)