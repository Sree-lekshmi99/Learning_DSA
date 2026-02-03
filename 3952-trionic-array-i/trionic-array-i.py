from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # 1) strictly increasing: nums[0..p]
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        p = i
        if p == 0:              # need 0 < p
            return False

        # 2) strictly decreasing: nums[p..q]
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        q = i
        if q == p:              # need p < q (must decrease at least once)
            return False

        # 3) strictly increasing: nums[q..n-1]
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # must reach the end, and also q < n-1 (final inc has at least one step)
        return i == n - 1 and q < n - 1
