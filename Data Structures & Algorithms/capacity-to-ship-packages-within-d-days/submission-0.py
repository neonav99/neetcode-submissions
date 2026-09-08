class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:

            cap = (l+r) // 2

            if self.minCapacityFinder(cap,weights,days):
                r = cap

            else:
                l = cap + 1

        return r

    def minCapacityFinder(self,capacity,weights,days):
        current_weight = 0
        days_taken = 1

        for weight in weights:
            current_weight += weight
            if current_weight > capacity:
                days_taken += 1
                current_weight = weight

        return days_taken <= days

        