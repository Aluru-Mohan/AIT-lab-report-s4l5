import numpy as np
import random

n_ants = 5
n_iterations = 100
decay = 0.01
alpha = 1
beta = 2

distance_matrix = np.array([
    [0, 10, 18, 20, 25],
    [10, 0, 31, 25, 17],
    [18, 31, 0, 28, 23],
    [20, 25, 28, 0, 23],
    [25, 17, 23, 23, 0]
])

n = len(distance_matrix)
pheromone = np.ones((n, n)) / n
all_inds = range(n)

def pick_move(pheromone_row, dist_row, visited):
    pheromone_row = np.copy(pheromone_row)
    pheromone_row[list(visited)] = 0
    row = pheromone_row ** alpha * ((1.0 / dist_row) ** beta)
    norm_row = row / row.sum()
    move = np.random.choice(all_inds, 1, p=norm_row)[0]
    return move

def gen_path(start):
    path = []
    visited = set([start])
    prev = start
    for _ in range(n - 1):
        move = pick_move(pheromone[prev], distance_matrix[prev], visited)
        path.append((prev, move))
        prev = move
        visited.add(move)
    path.append((prev, start))
    return path

def path_distance(path):
    total = 0
    for (i, j) in path:
        total += distance_matrix[i][j]
    return total

def run_aco():
    global pheromone
    shortest_path = None
    all_time_shortest = (None, np.inf)
    for _ in range(n_iterations):
        all_paths = []
        for _ in range(n_ants):
            path = gen_path(0)
            dist = path_distance(path)
            all_paths.append((path, dist))
        all_paths.sort(key=lambda x: x[1])
        if all_paths[0][1] < all_time_shortest[1]:
            all_time_shortest = all_paths[0]
        pheromone = pheromone * (1 - decay)
        for path, dist in all_paths[:n_ants]:
            for move in path:
                pheromone[move] += 1.0 / distance_matrix[move]
    return all_time_shortest

shortest_path = run_aco()

print("\nDistance Matrix (Travel Times):")
print(distance_matrix)
print("\nOptimized Ride Sharing Route:")
print(shortest_path[0])
print("\nShortest Duration:", shortest_path[1], "minutes")
