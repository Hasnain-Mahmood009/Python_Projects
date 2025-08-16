class Solution:
    def maximum69Number (self, num: int) -> int:
        max_num = 0
        li = list(str(num))
        for i in range(len(li)):
            if li[i] == "6":
                li[i] = "9"
                break
        return int("".join(li))