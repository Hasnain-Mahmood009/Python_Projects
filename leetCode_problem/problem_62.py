class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}

        for ch in s:
            char_count[ch] = char_count.get(ch,0) + 1

        for ch in t:
            if ch not in char_count or char_count[ch] == 0:
                return False
            char_count[ch] -= 1
        
        return True