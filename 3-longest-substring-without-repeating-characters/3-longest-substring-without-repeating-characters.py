class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        found_chars={}
        least_index=0
        max_counter=0
        counter=0

        i=0
        while i < len(s):
            if  s[i] in  found_chars.keys():
                print("i : ",i)
                print("least_index : ",least_index)
                counter=i-least_index
                least_index=found_chars[s[i]]+1
                for key in list(found_chars.keys()):
                    if found_chars[key]<found_chars[s[i]]:
                        del found_chars[key]
            else:
                counter=(i-least_index)+1
            found_chars[s[i]]=i
                
            if counter>max_counter:
                max_counter=counter
            if max_counter==95:
                i=len(s)
            i+=1
        if not counter:
            max_counter=len(s)
        return max_counter