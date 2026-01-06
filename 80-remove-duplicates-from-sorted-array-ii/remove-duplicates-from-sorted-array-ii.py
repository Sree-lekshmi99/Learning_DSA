class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 0
        count = defaultdict(int)
        for i in nums:
            count[i]+=1
            if count[i]<=2:
                nums[ans] = i
                ans+=1
        return len(nums[:ans])
            