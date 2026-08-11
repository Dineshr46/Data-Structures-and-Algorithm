class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            return (nums[n//2] + nums[n//2 -1]) / 2.0
        else:
            return nums[n//2]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        