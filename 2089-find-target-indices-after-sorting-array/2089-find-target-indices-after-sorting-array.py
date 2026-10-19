class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums) 
        L = []

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


        if target in nums :
            for i in range (n) :
                if nums[i] == target :
                    L.append(i)
        else :
            return L

        return L

