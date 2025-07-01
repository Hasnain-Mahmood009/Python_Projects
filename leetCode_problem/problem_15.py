class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        li = []
        convert = int("".join(map(str,digits)))
        add = convert+1
        st = str(add)
        for i in range(len(st)):
            integer = int(st[i])
            li.append(integer)
        return li
        