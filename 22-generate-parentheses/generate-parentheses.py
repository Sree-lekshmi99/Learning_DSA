class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1 = ()
        # 2= ()(), (())
        # 3= ()()(), ()(()), (())(), ((()))), (()())
        # 4 = ()()()(), (())(()), (((()))), ()((())), ((()))(), ()()(()),

        # (()))    open = 2   closed = 3 closed<open  open<n opeen == closed == n

        stack = []
        ans = []
        def backtrack(openP,closedP):
            if openP==n and closedP==n:
                ans.append(''.join(stack))
                return
            if openP<n:
                stack.append('(')
                backtrack(openP+1,closedP)
                stack.pop()
            if closedP < openP:
                stack.append(')')
                backtrack(openP,closedP+1)
                stack.pop()
        backtrack(0,0)
        return ans
            