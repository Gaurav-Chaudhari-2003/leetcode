class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        unique_chars = {}   # with last index ocuuring

        for i in range(0, len(s)):
            char = s[i]
            unique_chars.update({char : i})
        
        print(unique_chars)

        new_presenty = {}
        for key in unique_chars.keys():
            new_presenty.update({key : False})

        new_str = [s[0]]
        new_presenty.update({s[0]: True})


        for i in range(1, len(s)):
            current_char = s[i]
            print(f'current char: {current_char}')
            if new_str[-1] > current_char and new_presenty.get(current_char) == False:
                while i >= 0 and len(new_str) > 0 and unique_chars.get(new_str[-1]) > i and new_str[-1] > current_char:
                        print(f'Before : {new_str} , {new_presenty}')
                        # new_str = new_str[:len(s)-1] + current_char
                        new_presenty.update({new_str.pop(): False})
                
                new_str.append(current_char)
                new_presenty.update({current_char: True})
                print(f'After : {new_str} , {new_presenty}')
                
            if new_presenty.get(current_char) == False:
                print(f'Before : {new_str} , {new_presenty}')
                new_str.append(current_char)
                new_presenty.update({current_char: True})
                print(f'After : {new_str} , {new_presenty}')
            
            print(f'new str: {new_str}')

        clean = ''
        for char in new_str:
            clean += char
        return clean