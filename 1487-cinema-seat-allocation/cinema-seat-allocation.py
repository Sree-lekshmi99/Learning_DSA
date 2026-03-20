class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        row_map = defaultdict(set)
        for row, col in reservedSeats:
            row_map[row].add(col)
        print(row_map)
        ans = (n-len(row_map))*2

        

        # combinations = [[2345],[4567],[6789]]

        for row, reserved in row_map.items():
            left =  all(seat not in reserved for seat in [2,3,4,5])
            right = all(seat not in reserved for seat in [6,7,8,9])
            mid = all(seat not in reserved for seat in [4,5,6,7])

            if left and right:
                ans+=2
            elif left or mid or right:
                ans+=1
        return ans
            



        


        