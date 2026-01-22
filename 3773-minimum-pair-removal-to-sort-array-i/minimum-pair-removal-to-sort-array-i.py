class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        n = len(nums)

        def sorted(nums):
            for i in range(1,len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True


        # heap = []
        
        while not sorted(nums):
            ops+=1
            min_sum = float('inf')
            pos =-1
            for i in range(len(nums)-1):
                curr_sum = nums[i+1] + nums[i]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    pos = i
            nums[pos] = min_sum
            del nums[pos+1]
        return ops

            