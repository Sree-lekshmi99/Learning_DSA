class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = k
        for i in nums:
            if i == count:
                count+=k
        return count
    
        