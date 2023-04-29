# A class defining Binary Indexed Tree:
class BIT:
    def __init__(self, maxN):
        self.maxN = maxN
        self.bit = [0] * (maxN + 1)
    def prefSum(self, n):
        ''' return prefix sum; allowed n=-1 for no prefix'''
        ret = 0
        n += 1
        while n > 0:
            ret += self.bit[n]
            n -= n & (-n)
        return ret
    def insert(self, v, delta):
        v += 1
        while v <= self.maxN:
            self.bit[v] += delta
            v += v & (-v)
