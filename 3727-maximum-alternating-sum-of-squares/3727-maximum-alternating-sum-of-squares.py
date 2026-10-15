class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        score = 0
        L = []


        for i in range (n) :
            L.append(abs(nums[i]))


        L.sort()


        if (n > 1) :
            for i in range (0, n // 2) :
                score += (L[n-1-i] ** 2) - (L[i] ** 2)
            if (n % 2 == 1) :
                score += L[n // 2] ** 2
        else :
            score += L[0] ** 2

        return score 

