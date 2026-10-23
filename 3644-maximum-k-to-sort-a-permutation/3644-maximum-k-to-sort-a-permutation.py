class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = [x for i, x in enumerate(nums) if x != i ]
        if not L :
            return 0      
        k = L[0]
        for x in L[1:] :
            k &= x
            if k == 0 :
                return 0
        return k