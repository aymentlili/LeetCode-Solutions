class Solution(object):
    def sortPermutation(self, n):
        k = -1
        for i, x in enumerate(n) :
            if x != i :
                k &= x
        return max(k, 0)