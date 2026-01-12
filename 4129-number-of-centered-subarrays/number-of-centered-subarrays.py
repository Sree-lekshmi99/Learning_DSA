class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        prefix_sum = [0]
        curr = 0
        for i in range(len(nums)):
            curr+=nums[i]
            prefix_sum.append(curr)
        print(prefix_sum)

        centered = 0
        for i in range(len(nums)):
            seen = set()
            for r in range(i,len(nums)):
                seen.add(nums[r])
                sub_sum = prefix_sum[r+1] - prefix_sum[i]
                if sub_sum in seen:
                    centered+=1
        print(centered)
        return centered
        