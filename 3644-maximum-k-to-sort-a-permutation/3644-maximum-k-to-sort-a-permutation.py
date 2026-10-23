class Solution(object):
    def sortPermutation(self, n):
        L = [x for i, x in enumerate(n) if x != i ]
        k = -1
        for x in L :
            k &= x
        return max(k, 0)