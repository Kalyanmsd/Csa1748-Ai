import math

# Minimax function to calculate the best possible outcome
def minimax(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 0 or node_index >= len(values):
        return values[node_index]
    if maximizing_player:
        best_value = -math.inf
        for i in range(2):
            val = minimax(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            best_value = max(best_value, val)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = math.inf
        for i in range(2):
            val = minimax(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            best_value = min(best_value, val)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value
values = [3, 5, 2, 9, 12, 5, 23, 23]  
tree_depth = math.log2(len(values))
best_score = minimax(depth=int(tree_depth), node_index=0, maximizing_player=True, values=values, alpha=-math.inf, beta=math.inf)

print(f"The optimal value is: {best_score}")
