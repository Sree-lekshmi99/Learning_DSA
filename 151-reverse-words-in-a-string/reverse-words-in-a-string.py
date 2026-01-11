class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()

        print(arr)
        return " ".join(arr[::-1])