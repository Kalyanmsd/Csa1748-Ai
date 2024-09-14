from itertools import permutations
def calculate_route_cost(graph, route):
    cost = 0
    for i in range(len(route) - 1):
        cost += graph[route[i]][route[i+1]]
    cost += graph[route[-1]][route[0]]  
    return cost
def tsp(graph, start=0):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)
    min_cost = float('inf')
    best_route = None
    for perm in permutations(cities):
        route = [start] + list(perm)
        current_cost = calculate_route_cost(graph, route)
        if current_cost < min_cost:
            min_cost = current_cost
            best_route = route
    return best_route, min_cost
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start_city = 0
best_route, min_cost = tsp(graph, start_city)
print(f"The best route is: {best_route}")
print(f"The minimum cost is: {min_cost}")
