class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, ans = 0, len(height) - 1, 0
        while l < r:
            if height[l] < height[r]:
                tmp = (r - l) * height[l]
                l += 1
            else:
                tmp = (r - l) * height[r]
                r -= 1
            if tmp > ans:
                ans = tmp
        return ans