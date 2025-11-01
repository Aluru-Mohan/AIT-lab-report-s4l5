import heapq

class Node:
    def _init_(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  # cost from start to current node
        self.h = h  # heuristic cost to goal
        self.f = g + h  # total cost

    def _lt_(self, other):
        return self.f < other.f


def a_star(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start, None, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue

            g = current_node.g + cost
            h = heuristics[neighbor]
            node = Node(neighbor, current_node, g, h)

            skip = False
            for open_node in open_list:
                if open_node.name == neighbor and open_node.f <= node.f:
                    skip = True
                    break
            if skip:
                continue

            heapq.heappush(open_list, node)

    return None



graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'D': 1},
    'D': {'E': 6, 'F': 5},
    'E': {'F': 2},
    'F': {'G': 1},
    'G': {}
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

path = a_star(graph, heuristics, 'A', 'G')
print("Shortest path:", path)
