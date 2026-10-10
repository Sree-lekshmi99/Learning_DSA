class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = []
        max_kid = max(candies)
        for i in range(len(candies)):
            curr_kid = candies[i]+ extraCandies
            if curr_kid >= max_kid:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        