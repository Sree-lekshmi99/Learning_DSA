class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            checker = set()
            for j in range(i,len(nums)):
                checker.add(nums[j])
                res+=len(checker)**2
        return res

        