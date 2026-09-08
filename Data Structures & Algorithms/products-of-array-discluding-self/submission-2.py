class Solution:

    def multiple(self, nums:List[int]):
        product = 1
        for n in nums:
            if n == 0:
                return 0
            product *= n
        return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_val = []
        len_nums = len(nums)
        for index in range(len_nums):
            left_part = nums[:index]
            right_part = nums[index + 1:]
            product = self.multiple(left_part + right_part)
            list_val.append(product)
        
        return list_val
        

        
                
            