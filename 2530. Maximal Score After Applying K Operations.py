import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        ans = 0
        for i in range(k):
            val = -(heapq.heappop(heap))
            ans += val
            heapq.heappush(heap, -ceil(val/3))
        return ans