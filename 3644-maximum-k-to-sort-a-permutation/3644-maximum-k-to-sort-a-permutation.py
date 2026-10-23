class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        L = []

        for i in range(n) :
            if nums[i] != i :
                L.append(nums[i])

        if (L == []) :
            return 0
        
        k = L[0]
        

        for x in L[1:] :
            k &= x
            if k == 0 :
                return 0
        
        return k