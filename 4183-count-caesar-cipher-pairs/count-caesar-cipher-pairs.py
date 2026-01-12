class Solution:
    def countPairs(self, words: List[str]) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        count =  defaultdict(int)
        ans = 0
        # blueprint
        for ch in words:
            first_letter = letters.index(ch[0])
            blueprint = tuple((letters.index(c)-first_letter)%26 for c in ch)
            count[blueprint]+=1


        for b,c in count.items():
            ans+=c*(c-1)//2
        print(ans)
        return ans

        
        

        
        