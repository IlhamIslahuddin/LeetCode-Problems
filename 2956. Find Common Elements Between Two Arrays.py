class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1 = 0
        answer2 = 0
        for i in range (len(nums1)):
            if nums1[i] in nums2:
                answer1 += 1
        for i in range (len(nums2)):
            if nums2[i] in nums1:
                answer2 += 1
        return [answer1, answer2]
