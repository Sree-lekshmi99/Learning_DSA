class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        ans = [1]*(len(nums))
        # ans1 = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = prefix
            prefix*=nums[i]
        print(ans)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=postfix
            postfix *= nums[i]
            
        # print(ans1)
        return ans

        