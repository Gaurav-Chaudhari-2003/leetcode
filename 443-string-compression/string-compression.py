class Solution:
    def compress(self, chars: list[str]) -> int:
        
        chars_dict = []

        prev_char = chars[0]
        current_count = 0
        for current_char in chars:
            if current_char != prev_char:
                chars_dict += [prev_char, current_count]

                prev_char = current_char
                current_count=1
            else:
                current_count+=1
        
        chars_dict += [prev_char, current_count]
            
        print(chars_dict)        

        ptr = 0
        for item in chars_dict:
            if type(item) == type(''):
                if ptr >= len(chars):
                    chars.append(item)
                else:
                    chars[ptr] = item
                ptr += 1
            elif type(item) == type(3) and item != 1:
                for char in f'{item}':
                    if ptr >= len(chars):
                        chars.append(char)
                    else:
                        chars[ptr] = char
                    ptr += 1
                
            
        print(chars)
                
        return ptr