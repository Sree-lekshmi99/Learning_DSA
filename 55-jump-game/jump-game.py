class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas  = 0
        n = len(nums)
        i = 0
        if len(nums) == 1:
            return True
        for i in nums:           
            if gas<0:
                return False
            elif gas<i:
                gas = i
            gas-=1
        return True
        