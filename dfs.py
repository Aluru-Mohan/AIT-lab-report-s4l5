graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]  

    while stack:
        node = stack.pop()  
        if node not in visited:
            print(node,end="")
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

print("Following is the Depth-First Search using a proper stack:")
dfs_iterative(graph, '5')
