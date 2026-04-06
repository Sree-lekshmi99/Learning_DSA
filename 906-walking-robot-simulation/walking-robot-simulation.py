class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        cord = [0,0]
        x,y = cord
        direction = 'N'
        max_dist = 0
        obstacles = set(map(tuple, obstacles))
        def turn(current, neg):
            right_turn = {"N": "E", "E": "S", "S": "W", "W": "N"}
            left_turn = {"N": "W", "W": "S", "S": "E", "E": "N"}

            if neg == -1:
                return right_turn[current]
            elif neg == -2:
                return left_turn[current]

        for i in range(len(commands)):
            # x , y = cord
            if commands[i]<0:
                direction = turn(direction,commands[i])
            elif direction == 'N':
                temp = commands[i]
                while temp:
                    next_x , next_y = x , y
                    next_y+=1
                    if (next_x, next_y) in obstacles:
                        break
                    cord = [next_x,next_y]
                    x , y = cord
                    temp-=1
            elif direction == 'E':
                temp = commands[i]
                while temp:
                    next_x , next_y = x , y
                    next_x+=1
                    if (next_x, next_y) in obstacles:
                        break
                    cord = [next_x,next_y]
                    x , y = cord
                    temp-=1
            elif direction == 'S':
                temp = commands[i]
                # x , y = cord
                while temp:
                    next_x , next_y = x , y
                    next_y-=1
                    # temp-=1
                    if (next_x, next_y) in obstacles:
                        break
                    cord = [next_x,next_y]
                    x , y = cord
                    temp-=1
            elif direction == 'W':
                temp = commands[i]
                # x , y = cord
                while temp:
                    next_x , next_y = x , y
                    next_x-=1
                    # temp-=1
                    if (next_x, next_y) in obstacles:
                        break
                    cord = [next_x,next_y]
                    x , y = cord
                    temp-=1
            max_dist = max(max_dist, cord[0]**2 + cord[1]**2)
        return max_dist
        
                    




                


        