class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        l = [None] * len(height)
        r = [None] * len(height)
        l[0], r[-1] = height[0], height[-1]
        for i in range(1, len(height)):
            l[i], r[-i - 1] = max(l[i - 1], height[i]), max(r[-i], height[-i - 1])
        ans = 0
        for i in range(len(height)):
            ans += min(l[i], r[i]) - height[i]
        return ans