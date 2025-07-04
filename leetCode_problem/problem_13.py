class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
