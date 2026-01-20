class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            temp = num
            count = 0
            if num & 1 == 0:
                ans.append(-1)
            else:
                while num & 1 == 1:
                    count+=1
                    num >>=1
                    # print(count)
                smallest = temp - 2**(count-1)
                ans.append(smallest)
            print(ans)
        return ans
            

        