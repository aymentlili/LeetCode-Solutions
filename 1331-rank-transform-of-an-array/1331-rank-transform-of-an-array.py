class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        SL = sorted(set(arr))
        
        rank = {x: i + 1 for i, x in enumerate(SL)}
        
        return [rank[x] for x in arr]