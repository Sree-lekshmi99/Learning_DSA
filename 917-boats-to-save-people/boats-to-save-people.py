class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        l = 0
        r = len(people)-1
        people.sort()
        while l<=r:
            temp = people[l]+people[r]
            if temp<=limit:
                l+=1
            r-=1
            boat+=1
        return boat
        # if len(people) == 2:
        #     if sum(people) <= limit:
        #         return 1
        #     else:
        #         return 2
        # while r<len(people):     
        #     temp = 0
        #     if people[l] == limit:         
        #         boat+=1
        #         l+=1
        #         r+=1
        #     temp = people[l] + people[r]
        #     # print(temp)
        #     if temp > limit:
        #         boat+=1
        #         l+=1
        #         r+=1
        #     elif temp == limit:
        #         l+=2
        #         r+=2
        #         boat+=1
        # return boat+1
    


        
                
            




        
            
        