from collections import deque
class State:
    def __init__(self, missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_left = boat_left 
        self.missionaries_right = missionaries_right
        self.cannibals_right = cannibals_right
        self.parent = None  
    def is_valid(self):
        if self.missionaries_left >= 0 and self.cannibals_left >= 0 and self.missionaries_right >= 0 and self.cannibals_right >= 0:
            if (self.missionaries_left == 0 or self.missionaries_left >= self.cannibals_left) and (self.missionaries_right == 0 or self.missionaries_right >= self.cannibals_right):
                return True
        return False
    def is_goal(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0
    def __eq__(self, other):
        return self.missionaries_left == other.missionaries_left and self.cannibals_left == other.cannibals_left and self.boat_left == other.boat_left and self.missionaries_right == other.missionaries_right and self.cannibals_right == other.cannibals_right
    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat_left, self.missionaries_right, self.cannibals_right))
    def __str__(self):
        return f"Left(M={self.missionaries_left}, C={self.cannibals_left}) | Right(M={self.missionaries_right}, C={self.cannibals_right}) | Boat on {'left' if self.boat_left else 'right'} side"
def get_successors(state):
    successors = []
    if state.boat_left:  
        new_positions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  
        for m, c in new_positions:
            new_state = State(state.missionaries_left - m, state.cannibals_left - c, 0,
                              state.missionaries_right + m, state.cannibals_right + c)
            if new_state.is_valid():
                new_state.parent = state
                successors.append(new_state)
    else:  
        new_positions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in new_positions:
            new_state = State(state.missionaries_left + m, state.cannibals_left + c, 1,
                              state.missionaries_right - m, state.cannibals_right - c)
            if new_state.is_valid():
                new_state.parent = state
                successors.append(new_state)
    return successors
def bfs():
    initial_state = State(3, 3, 1, 0, 0)
    if initial_state.is_goal():
        return initial_state
    frontier = deque([initial_state])
    explored = set()
    while frontier:
        state = frontier.popleft()
        if state in explored:
            continue
        explored.add(state)
        for successor in get_successors(state):
            if successor.is_goal():
                return successor
            frontier.append(successor)
    return None
def print_solution(solution):
    path = []
    state = solution
    while state:
        path.append(state)
        state = state.parent
    path.reverse()
    for step in path:
        print(step)
solution = bfs()
if solution:
    print("Solution found:")
    print_solution(solution)
else:
    print("No solution found.")
