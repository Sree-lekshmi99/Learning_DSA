class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # -14 -10 -4 3 8 19 23 27
        pairs = []
        min_diff = float('inf')
        arr.sort()
        for i in range(len(arr)-1):
            diff = abs(arr[i+1] - arr[i])
            if diff < min_diff:
                min_diff = diff
                pairs = []
            if min_diff == abs(arr[i+1] - arr[i]):
                pairs.append([arr[i],arr[i+1]])
        return pairs


