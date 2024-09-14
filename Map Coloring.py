# Map Coloring Problem using CSP (Backtracking)
def is_valid(assignment, region, color, neighbors):
    for neighbor in neighbors[region]:
        if assignment.get(neighbor) == color:
            return False
    return True
def csp_backtracking(assignment, regions, colors, neighbors):
    if len(assignment) == len(regions):
        return assignment
    for region in regions:
        if region not in assignment:
            for color in colors:
                if is_valid(assignment, region, color, neighbors):
                    assignment[region] = color
                    result = csp_backtracking(assignment, regions, colors, neighbors)
                    if result:
                        return result
                    del assignment[region]
            return None
def map_coloring():
    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    colors = ["Red", "Green", "Blue"]
    neighbors = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": []  
    }
    assignment = {}
    result = csp_backtracking(assignment, regions, colors, neighbors)
    if result:
        print("Coloring Solution Found:")
        for region, color in result.items():
            print(f"{region}: {color}")
    else:
        print("No solution found")
map_coloring()
