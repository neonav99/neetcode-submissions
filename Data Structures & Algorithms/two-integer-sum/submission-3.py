class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index,number in enumerate(nums):
            complement = target - number
            if complement in seen:
                if index<nums.index(complement):
                    return[index,nums.index(complement)]
                else:
                    return[nums.index(complement),index]
            seen[number] = True
        
        return None
