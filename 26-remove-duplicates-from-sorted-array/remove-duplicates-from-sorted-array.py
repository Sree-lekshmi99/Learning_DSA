class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans  = 0
        count = Counter(nums)
        for a, i in count.items():
            nums[ans] = a
            ans+=1



        return ans
