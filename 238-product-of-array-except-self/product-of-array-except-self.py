class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        ans2 = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *=nums[i]
        print(ans)

        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            ans2[i] = suffix
            suffix*=nums[i]
        print(ans2)

        for i in range(len(nums)):
            ans[i] = ans[i]*ans2[i]
        return ans

            
        