class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_app = {}
        l = 0;
        ans = 0;
        for r, ch in enumerate(s):
            if ch in last_app:
                if (l < last_app[ch] + 1):
                    l = last_app[ch] + 1
                last_app[ch] = r
            else:
                last_app[ch] = r
            print l
            length = r - l + 1
            if length > ans:
                ans = r - l + 1
        return ans