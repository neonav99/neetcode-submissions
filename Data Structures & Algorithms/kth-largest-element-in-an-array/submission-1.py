class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        kth = 0
        heapq.heapify(nums)
        
        for _ in range(k):
            kth = heapq.heappop(nums)
        return -kth