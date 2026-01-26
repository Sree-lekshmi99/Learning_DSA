class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 1479
        # temp = []
        nums.sort()
        min_diff = float('inf')
        # diff = 0
        # l = 0
        for r in range(len(nums)-k+1):
                diff = nums[r+k-1] - nums[r] 
                min_diff = min(min_diff, diff)

        return min_diff
