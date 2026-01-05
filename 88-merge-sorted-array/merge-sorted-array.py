class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m+n
        # i = j = 0
        # if m>0 and n==0:
        #     return nums1
        # if m==0 and n>0:
        #     return nums2
        while m>0 and n>0          :
            if nums1[m-1]<=nums2[n-1]:
                nums1[a-1] = nums2[n-1]
                n-=1
            else:
                nums1[a-1] = nums1[m-1]
                m-=1
            a-=1
        while n>0:
            nums1[a-1] = nums2[n-1]
            n-=1
            a-=1

        
        print(nums1)



        