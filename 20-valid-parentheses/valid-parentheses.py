class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                continue
                
            if len(stack) > 0:
                if char == ')':
                    # stack.pop() if stack[-1] == '(' else return False 
                    # return False if stack[-1] != '(' else stack.pop()
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False

                elif char == ']': 
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                
                elif char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else: 
                        return False
            else:
                return False
        
        return len(stack) == 0
