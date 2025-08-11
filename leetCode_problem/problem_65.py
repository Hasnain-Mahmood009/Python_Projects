class Solution:
    def productQueries(self, n, queries):
        mod = 10**9 + 7
        powers = []
        bit = 0
        while n:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1
        powers.sort()
        res = []
        for l, r in queries:
            prod = 1
            for i in range(l, r + 1):
                prod = (prod * powers[i]) % mod
            res.append(prod)
        return res
