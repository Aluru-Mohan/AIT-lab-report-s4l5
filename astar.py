class Graph:
    def __init__(self, adjacency_list, heuristic):
        self.adjacency_list = adjacency_list  
        self.heuristic = heuristic  

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def h(self, node):
        """Heuristic function: estimated cost from node to goal"""
        return self.heuristic.get(node, float('inf'))

    def a_star(self, start_node, goal_node):
        open_list = set([start_node])  
        closed_list = set()  
        g = {start_node: 0}  
        parents = {start_node: None}  

        while open_list:
            current = min(open_list, key=lambda n: g[n] + self.h(n))

            if current == goal_node:
                path = []
                while current:
                    path.append(current)
                    current = parents[current]
                path.reverse()
                print("Final path:", path)
                print("Closed list (visited nodes):", closed_list)
                print("Cost g to goal:", g[goal_node])
                return path

            open_list.remove(current)
            closed_list.add(current)

            for neighbor, weight in self.get_neighbors(current):
                if neighbor in closed_list:
                    continue
                tentative_g = g[current] + weight
                if neighbor not in open_list:
                    open_list.add(neighbor)
                elif tentative_g >= g.get(neighbor, float('inf')):
                    continue
                parents[neighbor] = current
                g[neighbor] = tentative_g

            print(f"Evaluated node: {current}, g={g[current]}, h={self.h(current)}, f={g[current] + self.h(current)}")

        print("No path found!")
        return None

adjacency_list = {
    'S': [('A', 2), ('B', 3)],
    'A': [('G', 1)],
    'B': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 5,
    'A': 2,
    'B': 3,
    'G': 0
}
