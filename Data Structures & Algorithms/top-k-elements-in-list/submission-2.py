class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        heap = []

        for val in seen:
            heapq.heappush(heap,(seen[val],val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

        