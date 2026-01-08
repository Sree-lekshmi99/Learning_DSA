class Solution:
    def jump(self, nums: List[int]) -> int:
        jump=0
        farthest = 0
        cur = 0
        for i in range(len(nums)-1):
            farthest = max(farthest,i+nums[i])
            if cur == i:
                cur = farthest
                jump+=1

        return jump
