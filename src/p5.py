class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = {}
        max_len = 1
        ans = 0
        for i in xrange(len(s)):
            dp[i, i] = True
        for i in xrange(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i, i + 1] = True
                if max_len == 1:
                    max_len = 2
                    ans = i
            else:
                dp[i, i + 1] = False

        for k in xrange(3, len(s) + 1):
            for l in xrange(len(s) - k + 1):
                r = l + k - 1
                if s[l] == s[r] and (dp[l + 1, r - 1]):
                    dp[l, r] = True
                    if k > max_len:
                        max_len = k
                        ans = l
                else:
                    dp[l, r] = False
        return s[ans: ans + max_len]
