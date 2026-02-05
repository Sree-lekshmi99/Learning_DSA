class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        # n = len(nums)
        # for i in range(len(nums)):
        #     if nums[i]>0:
        #         idx = i + nums[i]
        #         if idx < n:
        #             result[i] = nums[idx]
        #         else:
        #             new_idx = n - idx
        #             result[i] = nums[new_idx]
        #     elif nums[i] < 0:
        #         idx = i - abs(nums[i])
        #         if idx <0:
        #             new_idx = n - idx
        #             result[i] = nums[new_idx]
        #         else:
        #             result[i] = nums[idx]
        #     if nums[i] == 0:
        #         result[i] = nums[i]
        # return result        
        n = len(nums)
        result = [0] * n

        for i, x in enumerate(nums):
            if x == 0:
                result[i] = 0
            else:
                result[i] = nums[(i + x) % n]

        return result