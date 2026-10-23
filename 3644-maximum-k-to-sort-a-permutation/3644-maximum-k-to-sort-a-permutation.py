class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = [x for i, x in enumerate(nums) if x != i ]
        k = -1
        for x in L :
            k &= x
        return k if k != -1 else 0