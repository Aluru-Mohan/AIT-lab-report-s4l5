

graph = {
    'A': {'B': 2},
    'B': {'C': 3},
    'C': {'D': 1},
    'D': {'A': 4}
}

def path1():
    start, end = 'A', 'A'
    path = ['A', 'B', 'C', 'D', 'A']
    total_cost = 0
    print(f"Costs of edges from {start} to {end}:")
    
    for i in range(len(path) - 1):
        src = path[i]
        dst = path[i + 1]
        cost = graph[src][dst]
        print(f"Edge {src} -> {dst} cost of cost {cost}")
        total_cost += cost

    print(f"Total cost from {start} to {end}: {total_cost}")


def path2():
    src, dst = 'A', 'D'
    path = ['A', 'B', 'C', 'D']
    total_cost = 0
    print(f"Costs of edges from {src} to {dst}:")

    for i in range(len(path) - 1):
        s = path[i]
        d = path[i + 1]
        cost = graph[s][d]
        print(f"Edge {s} -> {d} cost of cost {cost}")
        total_cost += cost

    print(f"Total cost from {src} to {dst}: {total_cost}")
