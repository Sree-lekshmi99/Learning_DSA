class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = ''
        res= ''
        invert = ''
        s = [0]*(n+1)
        for i in range(1, n+1):
            temp = format(i,"b")
            prev = str(s[i-1])
            
            invert = "".join('1' if x =='0' else '0' for x in prev)
            
            ans = prev + '1'+ invert[::-1]
            s[i] = str(ans)
            

        return s[n][k-1]



        