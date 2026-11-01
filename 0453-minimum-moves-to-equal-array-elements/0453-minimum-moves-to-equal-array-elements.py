class Solution(object):
    def minMoves(self, nums):
        if len(set(nums)) <= 1 :
            return 0
        return sum(nums) - len(nums) * min(nums)


