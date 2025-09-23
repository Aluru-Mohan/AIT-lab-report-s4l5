import networkx as nx
def a_star_pathfinding(graph, start_node, goal_node, heuristic):  
    try:
        path = nx.astar_path(graph, start_node, goal_node,
heuristic=heuristic, weight=&#39;weight&#39;)
        return path
    except nx.NetworkXNoPath:
        return None
# Example Usage:
if __name__ == &quot;__main__&quot;:
    # Create a sample graph
    G = nx.Graph()
    G.add_edge(&#39;A&#39;, &#39;B&#39;, weight=6)
    G.add_edge(&#39;A&#39;, &#39;F&#39;, weight=3)
    G.add_edge(&#39;B&#39;, &#39;C&#39;, weight=3)
    G.add_edge(&#39;B&#39;, &#39;D&#39;, weight=2)
    G.add_edge(&#39;C&#39;, &#39;E&#39;, weight=5)
    G.add_edge(&#39;D&#39;, &#39;E&#39;, weight=8)
    G.add_edge(&#39;F&#39;, &#39;G&#39;, weight=1)
    G.add_edge(&#39;G&#39;, &#39;H&#39;, weight=7)
    G.add_edge(&#39;H&#39;, &#39;I&#39;, weight=2)
    G.add_edge(&#39;E&#39;, &#39;I&#39;, weight=5)
    G.add_edge(&#39;I&#39;, &#39;J&#39;, weight=3)
    # Define a heuristic function (example: straight-line distance or
estimated cost)
    # In a real-world scenario, this would be more complex and domain-
specific.
    heuristic_values = {
        &#39;A&#39;: 11, &#39;B&#39;: 6, &#39;C&#39;: 5, &#39;D&#39;: 7, &#39;E&#39;: 3,
        &#39;F&#39;: 6, &#39;G&#39;: 5, &#39;H&#39;: 3, &#39;I&#39;: 1, &#39;J&#39;: 0
    }
    def example_heuristic(u, v):
        return heuristic_values.get(u, 0) # Simple example, usually
depends on v as well
    start = &#39;A&#39;
    goal = &#39;J&#39;
    path = a_star_pathfinding(G, start, goal, example_heuristic)
