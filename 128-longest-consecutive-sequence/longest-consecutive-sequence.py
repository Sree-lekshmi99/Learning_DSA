class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = set(nums)
        m_l = 0
        for num in cons:
            if num-1 not in cons:
                l = 1
                while num+l in cons:
                    l+=1
                m_l =max(m_l,l)
        return m_l
                
        print(cons)