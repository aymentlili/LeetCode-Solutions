class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Helper to compute sum of digits
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        # Sort pairs based on (digit_sum, val)
        sorted_pairs = sorted(
            [(val, i) for i, val in enumerate(nums)],
            key=lambda item: (digit_sum(item[0]), item[0])
        )

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or sorted_pairs[i][1] == i:
                continue

            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = sorted_pairs[curr][1]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps