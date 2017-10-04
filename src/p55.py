class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farest = 0
        n = len(nums)
        for i in range(n):
            if i <= farest:
                if i + nums[i] >= n - 1:
                    return True
                elif i + nums[i] > farest:
                    farest = i + nums[i]
        return False