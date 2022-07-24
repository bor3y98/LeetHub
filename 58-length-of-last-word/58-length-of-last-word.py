class Solution(object):
    def lengthOfLastWord(self, s):
        counter=0
        started=False
        ended=False
        for i in range(len(s)-1,-1,-1):
            if s[i] !=' ' and not ended:
                started=True
                counter +=1
            else:
                if started:
                    ended=True
                    break
        return counter
        """
        :type s: str
        :rtype: int
        """
        