class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if (n == 1) :
            return 0

        up = down = 1

        for i in range (1, n) :
            up += nums[i] == (nums[i - 1] + 1) % n
            down += nums[i - 1] == (nums[i] + 1) % n

        if up == n :
            return 0 if not nums[0] else min(n - nums[0], nums[0] + 2)

        if down == n:
            return min(n - nums[-1], nums[-1]) + 1

        return -1