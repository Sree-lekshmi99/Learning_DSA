class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        frq = defaultdict(list)
        for i in range(len(nums)):
            frq[nums[i]].append(i)
        print(frq)
        ans = float('inf')

        for num , idx in frq.items():
            if len(idx) >= 3:
                for t in range(len(idx) - 2):
                    ans = min(ans, 2 * (idx[t + 2] - idx[t]))
                # i, j , k = idx
                # temp =  abs(i - j) + abs(j - k) + abs(k - i)
                # if temp == 2*(k-i):
                    # return temp
        return ans if ans != float('inf') else -1

