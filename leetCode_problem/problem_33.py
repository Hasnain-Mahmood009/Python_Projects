class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = "".join(char.lower() for char in s if char.isalnum())
        rev = clean[::-1]
        if clean == rev:
            return True
        else:
            return False