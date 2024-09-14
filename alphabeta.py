import math

# Minimax function with Alpha-Beta pruning
def minimax(depth, node_index, is_maximizing_player, values, alpha, beta):
    if depth == 0 or node_index >= len(values):
        return values[node_index]
    if is_maximizing_player:
        best = -math.inf
        for i in range(2):
            value = minimax(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            value = minimax(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
values = [3, 5, 6, 9, 1, 2, 0, -1]  
tree_depth = math.log2(len(values))
alpha = -math.inf
beta = math.inf
best_value = minimax(int(tree_depth), 0, True, values, alpha, beta)
print(f"The optimal value is: {best_value}")
