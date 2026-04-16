class Solution:
    def encode(self, strs):
        char_arr = []
        for i_str in strs:
            for i, str_i in enumerate(i_str):
                ascii_i = ord(str_i)
                if i % 2 == 0:
                    d_ascii = chr(ascii_i + 3)
                else:
                    d_ascii = chr(ascii_i + 1)
                char_arr.append(d_ascii)

            # delimiter (fixed encoding)
            char_arr.append('অ')  # simpler delimiter

        return "".join(char_arr)

    def decode(self, s: str):
        decoded = []
        ind_str = []
        i = 0

        for ch in s:
            if ch == 'অ':
                decoded.append("".join(ind_str))
                ind_str = []
                i = 0  
                continue

            num = ord(ch)
            if i % 2 == 0:
                char = chr(num - 3)
            else:
                char = chr(num - 1)

            ind_str.append(char)
            i += 1

        return decoded
        
        
        
s = Solution() 
print(s.decode(s.encode(["Hello","World"])))
