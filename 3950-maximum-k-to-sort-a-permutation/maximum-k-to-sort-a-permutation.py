class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        for i, value in enumerate(nums):
            if value!=i:
                ans&=value
        return 0 if ans ==-1 else ans