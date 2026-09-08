class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_seq = 0

        for number in numset:
            if (number - 1) not in numset:
                length = 1
                while (number + length) in numset:
                    length+=1
                longest_seq = max(length, longest_seq)
        return longest_seq
        