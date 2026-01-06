class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        for val,c in count.items():
            if c > len(nums)/2:
                return val
        