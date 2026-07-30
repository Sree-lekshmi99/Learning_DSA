class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visited = set()
        for i in range(len(arr)):
            if arr[i]*2 in visited or (arr[i]%2==0 and arr[i]//2 in visited):
                return True
            visited.add(arr[i])
        return False
        