class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        even_id = {}
        odd_id = {}
        for x in nums:
            if x % 2 == 0:
                if x not in even_id:
                    even_id[x] = len(even_id)
            else:
                if x not in odd_id:
                    odd_id[x] = len(odd_id)

        ans = 0
        n = len(nums)

        for i in range(n):
            even_mask = 0
            odd_mask = 0
            for j in range(i, n):
                x = nums[j]
                if x % 2 == 0:
                    even_mask |= 1 << even_id[x]
                else:
                    odd_mask |= 1 << odd_id[x]

                if even_mask.bit_count() == odd_mask.bit_count():
                    ans = max(ans, j - i + 1)

        return ans        # right = 1
      