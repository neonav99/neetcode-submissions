class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = list(set(nums1))
        set_2 = list(set(nums2))

        ret_1 = []
        ret_2 = []

        for num in set_1:
            if num not in set_2:
                ret_1.append(num)
        for num in set_2:
            if num not in set_1:
                ret_2.append(num)

        return [ret_1,ret_2]



        