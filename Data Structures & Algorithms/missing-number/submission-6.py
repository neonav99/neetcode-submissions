class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_val = (len(nums)*(len(nums)+1))/2
        sum_nums = sum(nums)
        if 0 not in nums:
            return 0
    
        diff = int(total_val - sum_nums)
        if diff == 0:
            return len(nums) + 1
        else:
            return diff

            



        