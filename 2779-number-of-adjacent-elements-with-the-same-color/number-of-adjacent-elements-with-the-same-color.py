class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0]*n
        cur = 0
        ans=[]

        for i , color in queries:
            old = colors[i]
            if old>0:
                if i-1 >=0 and colors[i-1] == old:
                    cur-=1
                if i+1<n and colors[i+1] ==old:
                    cur-=1
            colors[i] = color
            
            if i - 1 >= 0 and colors[i - 1] == color:
                cur += 1
            if i + 1 < n and colors[i + 1] == color:
                cur += 1

            ans.append(cur)
                
            # ans[key] = values
            # if ans[key] == values and ans[key-1]==values and ans[key+1]== values
            
        return ans
        