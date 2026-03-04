class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        row_count = [sum(row) for row in mat]
        col_count = [sum(mat[r][c] for r in range(rows)) for c in range(cols)]

        count = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and row_count[r] == 1 and col_count[c] == 1:
                    count += 1

        return count