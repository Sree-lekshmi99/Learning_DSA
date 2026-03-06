class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # if len(s) == 1 and s == '1':
        #     return True
        # else:

        one_count = s.count('1')
        print(one_count)
        
        for i in range(len(s)-1):
            if s[i]== '1':
                one_count-=1
                l = i+1
                while one_count >0:
                    if s[l] == '1':
                        one_count-=1
                        l+=1
                    else:
                        return False if one_count else True
                if one_count == 0:
                    return True

                
        return True if len(s) == 1 and s[0] == '1' else False


                
                

        