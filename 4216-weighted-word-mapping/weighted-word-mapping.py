class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # l = {
        #     a:1,b:2,c:3,d:4,e:5,f:6,g:7
        # }
        res = 0
        ans = []
        for word in words:
            res = 0
            for i in range(len(word)):
                position = ord(word[i]) - 97
                res+= weights[position]

            res%=26
            ch = chr(ord('z') - res)
            ans.append(ch)
        return ''.join(ans)

        

        