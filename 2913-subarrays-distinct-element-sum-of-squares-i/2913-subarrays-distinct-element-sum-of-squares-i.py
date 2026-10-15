class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = 0


        for i in range (n) :
            L = set()
            for j in range (i, n) :
                L.add(nums[j])
                sum += len(L)**2                

        return sum


