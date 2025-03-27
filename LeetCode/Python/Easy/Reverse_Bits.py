class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            ret = ret << 1 
            ret += (n&1)
            n = n >> 1
        return ret