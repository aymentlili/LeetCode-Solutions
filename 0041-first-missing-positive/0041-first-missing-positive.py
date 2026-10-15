class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        i = 0
        while i < n:
            value = nums[i]
            target = value - 1
            if 1 <= value <= n and nums[target] != value:
                nums[i], nums[target] = nums[target], nums[i]
            else:
                i += 1

        for index, value in enumerate(nums, start=1):
            if value != index:
                return index

        return n + 1
