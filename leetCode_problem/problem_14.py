class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = []
        for i in range(len(s)-1,-1,-1):
            if len(li) == 0:
                if s[i] == " ":
                    continue
            if s[i] == " ":
                break
            else:
                li.append(s[i])
        
        return len(li)
            