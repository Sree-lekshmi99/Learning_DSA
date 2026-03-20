class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        # nums = set()
        
        diff = []

        def mindifference(nums):
            min_diff = float('inf')
            nums = sorted(nums)
            if len(nums)<2:
                return 0
            for i in range(len(nums)-1):
                min_diff = min(min_diff, abs(nums[i] - nums[i+1]))
            return min_diff

            


        for r in range(rows - k +1):
            row_result = []
            for c in range(cols-k+1):
                nums = set()
                for i in range(r , r+k):
                    
                    for j in range(c,c+k):

                        nums.add(grid[i][j])
                row_result.append(mindifference(nums))
            diff.append(row_result)
        return diff
                


        