class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {x: i + 1 for i, x in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]