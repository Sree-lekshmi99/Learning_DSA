class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r= len(numbers)-1
        while l<r:
            curr_Sum = numbers[l]+numbers[r]
            if curr_Sum == target:
                return [l+1,r+1]
            elif curr_Sum < target:
                l+=1
            else:
                r-=1
        
        