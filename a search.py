import heapq

# Class representing a single node in the grid
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic (estimated distance to goal)
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

# Heuristic function (Manhattan distance)
def heuristic(current, goal):
    return abs(current.position[0] - goal.position[0]) + abs(current.position[1] - goal.position[1])

# A* Search Algorithm
def astar(start, goal, grid):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, start)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # If we reach the goal, reconstruct the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate neighbors (4 directions)
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor_pos = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            # Check if neighbor is within the grid bounds and is walkable
            if 0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0]) and grid[neighbor_pos[0]][neighbor_pos[1]] == 0:
                neighbor = Node(neighbor_pos, current_node)

                if neighbor.position in closed_list:
                    continue

                # Calculate the g, h, and f values
                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h

                # Check if neighbor is in the open list with a higher cost
                if any(neighbor == node and neighbor.g > node.g for node in open_list):
                    continue

                heapq.heappush(open_list, neighbor)

    return None  # If no path is found

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = Node((0, 0))
goal = Node((4, 4))

path = astar(start, goal, grid)
if path:
    print("Path found:", path)
else:
    print("No path found")
