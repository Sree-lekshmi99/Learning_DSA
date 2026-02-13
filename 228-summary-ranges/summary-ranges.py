class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        ans= []
        while i <len(nums):
            start = nums[i]
            while i+1<len(nums) and nums[i]+1 == nums[i+1]:
                i+=1
            if start !=nums[i]:
                ans.append(f'{start}->{nums[i]}')
            else:
                ans.append(f'{nums[i]}')
            i+=1
        return ans
