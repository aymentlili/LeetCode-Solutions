class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {x: i + 1 for i, x in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]