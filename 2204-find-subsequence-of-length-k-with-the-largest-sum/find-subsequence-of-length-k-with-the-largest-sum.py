class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans = []
        max_heap  = []
        for i in range(len(nums)):
            heapq.heappush(max_heap, [-nums[i],i])
        print(max_heap)
        picked = [False] * len(max_heap)
        out = [None] * len(max_heap)
        while k:
            val , idx = heapq.heappop(max_heap)
            out[idx] = -val
            picked[idx] = True
            k-=1

        return [out[i] for i in range(len(nums)) if picked[i]]
