class Solution:
    def solveQueries(self, nums, queries):
        from collections import defaultdict
        import bisect
        
        n = len(nums)
        pos = defaultdict(list)
        
        # store indices of each value
        for i, x in enumerate(nums):
            pos[x].append(i)
        
        ans = []
        
        for q in queries:
            val = nums[q]
            indices = pos[val]
            
            if len(indices) == 1:
                ans.append(-1)
                continue
            
            i = bisect.bisect_left(indices, q)
            
            # neighbors in circular list
            left = indices[i - 1] if i > 0 else indices[-1]
            right = indices[i + 1] if i < len(indices) - 1 else indices[0]
            
            # circular distance
            d1 = min(abs(q - left), n - abs(q - left))
            d2 = min(abs(q - right), n - abs(q - right))
            
            ans.append(min(d1, d2))
        
        return ans