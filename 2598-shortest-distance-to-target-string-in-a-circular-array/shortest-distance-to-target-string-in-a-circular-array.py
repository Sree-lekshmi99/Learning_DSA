class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # min_dis = float('inf')
        # if target not in words:
        #     return -1
        n = len(words)
        for i in range((n//2)+1):
            if (words[(startIndex+i)%n] == target) or (words[(startIndex-i)%n]  == target):
                return i

        return -1
        
        