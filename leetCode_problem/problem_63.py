class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def signature(x):
            return ''.join(sorted(str(x)))

        sig_n = signature(n)

        for i in range(31):  
            if sig_n == signature(1 << i):
                return True
        return False
