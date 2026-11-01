class Solution(object):
    def minMoves(self, L):
        return sum(L) - len(L) * min(L)


