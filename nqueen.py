def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    def solve(row):
        if row == n:
            res.append(["".join("Q" if i == c else "." for i in range(n)) for c in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1
    res = []
    board = [-1] * n
    solve(0)
    return res
n = 4
for sol in solve_n_queens(n):
    for row in sol:
        print(row)
    print()
