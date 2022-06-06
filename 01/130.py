class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        ny,nx = len(board), len(board[0])
        queue = collections.deque()
        for yi in range(ny):
            queue.append((yi, 0))
            queue.append((yi, nx - 1))
        for xi in range(len(board[0])):
            queue.append((0, xi))
            queue.append((ny - 1, xi))
        while queue:
            yi, xi = queue.popleft()
            if 0 <= yi < ny and 0 <= xi < nx and board[yi][xi] == 'O':
                board[yi][xi] = 'P'
                queue.append((yi - 1, xi))
                queue.append((yi + 1, xi))
                queue.append((yi, xi - 1))
                queue.append((yi, xi + 1))
        for yi in range(ny):
            for xi in range(nx):
                if board[yi][xi] == 'P':
                    board[yi][xi] = 'O'
                else:
                    board[yi][xi] = 'X'