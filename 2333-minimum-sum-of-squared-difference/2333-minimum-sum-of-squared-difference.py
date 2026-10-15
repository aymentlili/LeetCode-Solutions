class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        if sum(d) <= k:
            return 0

        d.sort(reverse=True)
        d.append(0)
        n = len(nums1)

        for i in range(1, n + 1):
            cost = (d[i - 1] - d[i]) * i
            if cost > k:
                q, r = divmod(k, i)
                hi = d[i - 1] - q
                return (
                    hi * hi * (i - r)
                    + (hi - 1) * (hi - 1) * r
                    + sum(x * x for x in d[i:n])
                )
            k -= cost
        return 0


