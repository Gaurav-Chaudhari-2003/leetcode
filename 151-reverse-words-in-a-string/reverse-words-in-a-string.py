class Solution:
    def reverseWords(self, s: str) -> str:
        right = len(s) - 1
        left = right

        rev_string = ''

        while left >= 0:
            if s[left] == ' ':
                if left!=right:
                    if rev_string != '':
                        rev_string += ' '     
                    rev_string += f'{s[left+1:right+1]}'

                left -= 1
                right = left
            else:
                left -= 1
        else:
            if rev_string != '':
                rev_string += ' '     
            rev_string += f'{s[left+1:right+1]}'
        
        if rev_string[-1] == ' ':
            return rev_string[:len(rev_string)-1] 
        return rev_string