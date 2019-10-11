class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # time complexity O(m + n)
        # space complexity o(1)
        index1 = m-1
        index2 = n-1
        free = m+n-1

        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[free] = nums1[index1]
                index1 -= 1
                free -= 1
            else:
                nums1[free] = nums2[index2]
                index2 -= 1
                free -= 1

        while index2 >= 0:
            nums1[free] = nums2[index2]
            index2 -= 1
            free -= 1
