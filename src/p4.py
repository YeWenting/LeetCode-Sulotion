class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        min_i = max(0, (m+n) / 2 - n)
        max_i = min(m, (m+n) / 2)
        while min_i <= max_i:
            i = (min_i + max_i) / 2
            j = (m + n) / 2 - i
            if i > 0 and j < n and nums1[i-1] > nums2[j]:
                max_i = i - 1
            elif j > 0 and i < m and nums2[j-1] > nums1[i]:
                min_i = i + 1
            else:
                break
        if (m + n) % 2 == 1:
            if i == m:
                return nums2[j]
            if j == n:
                return nums1[i]
            else:
                return min(nums1[i], nums2[j])
        else:
            if i == 0:
                lnum = nums2[j-1]
            elif j == 0:
                lnum = nums1[i-1]
            else:
                lnum = max(nums1[i-1], nums2[j-1])
            if i == m:
                rnum = nums2[j]
            elif j == n:
                rnum = nums1[i]
            else:
                rnum = min(nums1[i], nums2[j])
            return float((lnum + rnum)) / 2

s = Solution()
print s.findMedianSortedArrays([], [1,2,3,4])