def manhattan_distance(puzzle):
    goal = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2) 
    }
    distance_sum = 0
    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]
            if value != 0:
                goal_position = goal[value]   
                distance = abs(i - goal_position[0]) + abs(j - goal_position[1])
                distance_sum += distance
    return distance_sum
puzzle = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]
distance_sum = manhattan_distance(puzzle)  
print(f"Manhattan Distance Sum: {distance_sum}")
