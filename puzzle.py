import heapq

class Puzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.n = len(board)
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def find_zero(self, board):
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == 0:
                    return i, j

    def neighbors(self, board):
        zero_x, zero_y = self.find_zero(board)
        for move_x, move_y in self.moves:
            x, y = zero_x + move_x, zero_y + move_y
            if 0 <= x < self.n and 0 <= y < self.n:
                new_board = [row[:] for row in board]
                new_board[zero_x][zero_y], new_board[x][y] = new_board[x][y], new_board[zero_x][zero_y]
                yield new_board

    def h(self, board):
        return sum(abs(i - goal_i) + abs(j - goal_j)
                   for i, row in enumerate(board)
                   for j, val in enumerate(row)
                   for goal_i, goal_row in enumerate(self.goal)
                   for goal_j, goal_val in enumerate(goal_row)
                   if val == goal_val and val != 0)

    def solve(self):
        queue = [(self.h(self.board), self.board, [], 0)]  # Add g(n) (number of moves) as the 4th element
        visited = set()
        while queue:
            f_cost, board, path, g_cost = heapq.heappop(queue)
            if board == self.goal:
                return path + [board], g_cost  # Return the path and the total cost
            visited.add(tuple(map(tuple, board)))
            for neighbor in self.neighbors(board):
                if tuple(map(tuple, neighbor)) not in visited:
                    new_g_cost = g_cost + 1
                    heapq.heappush(queue, (new_g_cost + self.h(neighbor), neighbor, path + [board], new_g_cost))

start = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

puzzle = Puzzle(start, goal)
solution, total_cost = puzzle.solve()

for step in solution:
    for row in step:
        print(row)
    print()

print(f"Total cost (number of moves): {total_cost}")
