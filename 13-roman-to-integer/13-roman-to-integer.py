class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        str_len=0
        result=0
        while str_len < len(s):
            if str_len == len(s)-1:
                result+=hash_map[s[str_len]] 
                str_len+=1
            else:
                if hash_map[s[str_len]] < hash_map[s[str_len+1]]:
                    result+=hash_map[s[str_len+1]] -hash_map[s[str_len]] 
                    str_len+=2
                else:
                    result+=hash_map[s[str_len]] 
                    str_len+=1
        return result