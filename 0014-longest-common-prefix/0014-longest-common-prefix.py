class Solution(object):
    def longestCommonPrefix(self, strs):

        x = strs[0]
        n = len(x)
        for s in strs :
            while x != s[0:n] :
                n -= 1
                x = x[0:n]
        return x